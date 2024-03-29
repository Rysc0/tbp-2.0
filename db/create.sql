
CREATE TABLE IF NOT EXISTS "Radno mjesto"
(
    "ID" serial NOT NULL,
    "Radno mjesto" text NOT NULL,
    CONSTRAINT "Radno mjesto_pkey" PRIMARY KEY ("ID")
);

CREATE TABLE IF NOT EXISTS "Plaća"
(
    "ID" serial NOT NULL,
    "Netto" double precision NOT NULL,
    "Brutto" double precision NOT NULL,
    "Zdravstveno" double precision NOT NULL,
    "Mirovinsko" double precision NOT NULL,
    "Putni trošak" double precision,
    "Total" double precision NOT NULL,
    CONSTRAINT "Plaća_pkey" PRIMARY KEY ("ID")
);

CREATE TABLE IF NOT EXISTS "Status"
(
    "ID" serial NOT NULL,
    "Status" text NOT NULL,
    CONSTRAINT "Status_pkey" PRIMARY KEY ("ID")
);

CREATE TABLE IF NOT EXISTS "Vozilo"
(
    "ID" serial NOT NULL,
    "Marka" text NOT NULL,
    "Reg. tablice" character varying(10) NOT NULL,
    "Vrijeme zadnjeg servisa" date NOT NULL,
    "Vrijeme idućeg servisa" date NOT NULL,
    "Vrijeme zadnje registracije" date NOT NULL,
    "Istek registracije" date NOT NULL,
    "Potrošnja" double precision NOT NULL,
    "Kilometraža" integer NOT NULL,
    "Zapremina rezervara" integer NOT NULL,
    CONSTRAINT "Vozilo_pkey" PRIMARY KEY ("ID")
);

CREATE TABLE IF NOT EXISTS "Trošak_Vrsta"
(
    "ID" serial NOT NULL,
    "Naziv" text NOT NULL,
    CONSTRAINT "Trošak_Vrsta_pkey" PRIMARY KEY ("ID")
);


CREATE TABLE IF NOT EXISTS "Zaposlenik"
(
    "ID" serial NOT NULL,
    "Ime i prezime" text NOT NULL,
    "Kontakt" text NOT NULL,
    "Plaća" integer NOT NULL,
    "Lozinka" text NOT NULL,
    "Email" text NOT NULL,
    "Radno vrijeme pocetak" time without time zone NOT NULL,
    "Radno vrijeme kraj" time without time zone NOT NULL,
    "Vozilo" integer,
    "Radno mjesto" integer NOT NULL,
    "Zaposlen" date NOT NULL,
    CONSTRAINT "Zaposlenik_pkey" PRIMARY KEY ("ID"),
    CONSTRAINT "Plaća" FOREIGN KEY ("Plaća")
        REFERENCES "Plaća" ("ID") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT "Radno mjesto" FOREIGN KEY ("Radno mjesto")
        REFERENCES "Radno mjesto" ("ID") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT "Vozilo iD" FOREIGN KEY ("Vozilo")
        REFERENCES "Vozilo" ("ID") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
);


CREATE TABLE IF NOT EXISTS "Isplata"
(
    "ID" serial NOT NULL,
    "ZaposlenikID" integer NOT NULL,
    "Datum" timestamp without time zone NOT NULL,
    "Plaća" integer NOT NULL,
    CONSTRAINT "Isplata_pkey" PRIMARY KEY ("ID"),
    CONSTRAINT "Plaća" FOREIGN KEY ("Plaća")
        REFERENCES "Plaća" ("ID") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT "ZaposlenikID" FOREIGN KEY ("ZaposlenikID")
        REFERENCES "Zaposlenik" ("ID") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
);

CREATE TABLE IF NOT EXISTS "WorkLog"
(
    "ZaposlenikID" integer NOT NULL,
    "Datum" date NOT NULL,
    "Status" integer NOT NULL,
    "Vozilo" integer,
    "Kilometraža" integer,
    "Dnevnik" text COLLATE pg_catalog."default",
    "ID" serial NOT NULL,
    CONSTRAINT "WorkLog_pkey" PRIMARY KEY ("ID"),
    CONSTRAINT "StatusiD" FOREIGN KEY ("Status")
        REFERENCES "Status" ("ID") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT "VoziloID" FOREIGN KEY ("Vozilo")
        REFERENCES "Vozilo" ("ID") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);


CREATE TABLE IF NOT EXISTS public."Trošak"
(
    "ID" serial NOT NULL,
    "Opis" text COLLATE pg_catalog."default",
    "Iznos" double precision NOT NULL,
    "Datum" date NOT NULL,
    "Vrsta" integer NOT NULL,
    "WorkLogID" integer NOT NULL,
    CONSTRAINT "Trošak_pkey" PRIMARY KEY ("ID"),
    CONSTRAINT "VrstaTroška" FOREIGN KEY ("Vrsta")
        REFERENCES public."Trošak_Vrsta" ("ID") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT "WorkLogID" FOREIGN KEY ("WorkLogID")
        REFERENCES public."WorkLog" ("ID") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);





CREATE OR REPLACE FUNCTION update_vehicle_kilometers()
RETURNS TRIGGER AS $$
BEGIN
    -- Fetch the corresponding vehicle ID from the WorkLog table
    -- and update the Kilometraža in the Vozilo table.
    UPDATE "Vozilo"
    SET "Kilometraža" = "Vozilo"."Kilometraža" + NEW."Kilometraža"
    WHERE "ID" = NEW."Vozilo";

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_update_vehicle_kilometers
AFTER INSERT ON "WorkLog"
FOR EACH ROW
EXECUTE FUNCTION update_vehicle_kilometers();








CREATE OR REPLACE FUNCTION calculate_placa_fields()
RETURNS TRIGGER AS $$
BEGIN
    -- Calculate Brutto, Zdravstveno, Mirovinsko, and Total
    NEW."Brutto" := ROUND((NEW."Netto" / 0.69)::numeric, 2);
    NEW."Zdravstveno" := ROUND((NEW."Brutto" * 0.16)::numeric, 2);
    NEW."Mirovinsko" := ROUND((NEW."Brutto" * 0.15)::numeric, 2);
    NEW."Total" := ROUND((NEW."Brutto" + COALESCE(NEW."Putni trošak", 0))::numeric, 2);

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_calculate_placa_fields
BEFORE INSERT ON "Plaća"
FOR EACH ROW
EXECUTE FUNCTION calculate_placa_fields();




-- Create the trigger function
CREATE OR REPLACE FUNCTION update_service_dates()
RETURNS TRIGGER AS $$
BEGIN
    -- Check if "Vrijeme idućeg servisa" has reached the given date
    IF NEW."Vrijeme idućeg servisa" <= CURRENT_DATE THEN
        -- Update "Vrijeme zadnjeg servisa" to the current value of "Vrijeme idućeg servisa"
        NEW."Vrijeme zadnjeg servisa" := NEW."Vrijeme idućeg servisa";
        
        -- Update "Vrijeme idućeg servisa" to be the same day in 3 months time
        NEW."Vrijeme idućeg servisa" := NEW."Vrijeme idućeg servisa" + INTERVAL '3 months';
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Create the trigger
CREATE TRIGGER trg_update_service_dates
BEFORE INSERT OR UPDATE ON "Vozilo"
FOR EACH ROW
EXECUTE FUNCTION update_service_dates();




-- Create the trigger function
CREATE OR REPLACE FUNCTION update_registration_dates()
RETURNS TRIGGER AS $$
BEGIN
    -- Check if "Vrijeme zadnje registracije" is today
    IF NEW."Vrijeme zadnje registracije" <= CURRENT_DATE THEN
        -- Update "Istek registracije" to be the same day in 1 year
        NEW."Istek registracije" := CURRENT_DATE + INTERVAL '1 year';
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Create the trigger
CREATE TRIGGER trg_update_registration_dates
BEFORE INSERT OR UPDATE ON "Vozilo"
FOR EACH ROW
EXECUTE FUNCTION update_registration_dates();


-- Create the trigger function
CREATE OR REPLACE FUNCTION generate_employee_info()
RETURNS TRIGGER AS $$
BEGIN
    -- Generate an email from "Ime i prezime"
    NEW."Email" := LOWER(REPLACE(TRANSLATE(NEW."Ime i prezime", ' ', '.'), 'ć', 'c') || '@example.com');
    
    -- Generate a random password
    NEW."Lozinka" := MD5(random()::TEXT);

    -- Set "Zaposlen" to the current date
    NEW."Zaposlen" := CURRENT_DATE;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Create the trigger
CREATE TRIGGER trg_generate_employee_info
BEFORE INSERT ON "Zaposlenik"
FOR EACH ROW
EXECUTE FUNCTION generate_employee_info();






INSERT INTO "Radno mjesto" ("Radno mjesto") VALUES
    ('Administrator'),
    ('Programmer'),
    ('HR Specialist'),
    ('Marketing Manager'),
    ('Accountant'),
    ('Sales Representative'),
    ('Customer Support'),
    ('Graphic Designer'),
    ('Project Manager'),
    ('System Analyst');


INSERT INTO "Vozilo" ("Marka", "Reg. tablice", "Vrijeme zadnjeg servisa", "Vrijeme idućeg servisa", "Vrijeme zadnje registracije", "Istek registracije", "Potrošnja", "Kilometraža", "Zapremina rezervara") VALUES
    ('Toyota Camry', 'ZG-123-AB', '2023-01-01', '2024-01-01', '2022-06-15', '2023-06-15', 8.5, 50000, 60),
    ('Ford Focus', 'ZG-678-BC', '2022-12-01', '2023-12-01', '2022-07-20', '2023-07-20', 7.2, 60000, 50),
    ('Honda Civic', 'ZG-543-CD', '2023-02-01', '2024-02-01', '2022-08-10', '2023-08-10', 6.8, 45000, 55);


INSERT INTO "Plaća" ("Netto", "Brutto", "Zdravstveno", "Mirovinsko", "Putni trošak", "Total") VALUES
    (2500.00, 3500.00, 150.00, 200.00, 50.00, 4000.00),
    (3000.00, 4200.00, 180.00, 250.00, 70.00, 4500.00),
    (3500.00, 5000.00, 200.00, 300.00, 80.00, 5300.00),
    (2800.00, 3800.00, 160.00, 220.00, 60.00, 4200.00),
    (3200.00, 4500.00, 190.00, 270.00, 75.00, 4800.00);

INSERT INTO "Status" ("Status") VALUES
    ('WFH'),
    ('In office'),
    ('On site'),
    ('Vacation'),
    ('Sick leave'),
	('Education');

INSERT INTO "Trošak_Vrsta" ("Naziv") VALUES
    ('Office Supplies'),
    ('Travel Expenses'),
    ('Training and Development'),
    ('Utilities'),
    ('Equipment Maintenance');

INSERT INTO "WorkLog" ("ZaposlenikID", "Datum", "Status", "Vozilo", "Kilometraža", "Dnevnik") VALUES
    (1, '2024-01-10', 1, 1, 50, 'Working on project A'),
    (2, '2024-01-11', 2, 2, 75, 'Attending training session'),
    (3, '2024-01-12', 3, NULL, NULL, 'On leave due to personal reasons'),
    (4, '2024-01-13', 1, 3, 60, 'Meeting with clients'),
    (5, '2024-01-14', 4, NULL, NULL, 'Waiting for project approval');

INSERT INTO "Trošak" ("Opis", "Iznos", "Datum", "Vrsta", "WorkLogID") VALUES
    ('Office Supplies', 150.00, '2024-01-10', 1, 1),
    ('Business Trip Expenses', 500.00, '2024-01-11', 2, 2),
    ('Training Workshop Fee', 200.00, '2024-01-12', 3, 3),
    ('Utilities Payment', 100.00, '2024-01-13', 4, 4),
    ('Equipment Maintenance', 300.00, '2024-01-14', 5, 5);

INSERT INTO "Zaposlenik" ("Ime i prezime", "Kontakt", "Plaća", "Lozinka", "Email", "Radno vrijeme pocetak", "Radno vrijeme kraj", "Vozilo", "Radno mjesto", "Zaposlen") VALUES
    ('John Doe', '091-234-5678', 1, 'password1', 'john.doe@example.com', '08:00:00', '17:00:00', 1, 1, '2024-01-01'),
    ('Jane Smith', '092-345-6789', 2, 'password2', 'jane.smith@example.com', '09:00:00', '18:00:00', 2, 2, '2024-01-02'),
    ('Michael Johnson', '093-456-7890', 3, 'password3', 'michael.johnson@example.com', '08:30:00', '17:30:00', 3, 3, '2024-01-03'),
    ('Emily Brown', '094-567-8901', 4, 'password4', 'emily.brown@example.com', '07:45:00', '16:45:00', NULL, 4, '2024-01-04'),
    ('David Davis', '095-678-9012', 5, 'password5', 'david.davis@example.com', '08:15:00', '17:15:00', NULL, 5, '2024-01-05'),
    ('Sarah White', '096-789-0123', 4, 'password6', 'sarah.white@example.com', '08:00:00', '17:00:00', NULL, 1, '2024-01-06'),
    ('Brian Wilson', '097-890-1234', 2, 'password7', 'brian.wilson@example.com', '09:30:00', '18:30:00', NULL, 2, '2024-01-07'),
    ('Lisa Miller', '098-901-2345', 1, 'password8', 'lisa.miller@example.com', '08:45:00', '17:45:00', NULL, 3, '2024-01-08'),
    ('Kevin Brown', '099-012-3456', 3, 'password9', 'kevin.brown@example.com', '08:00:00', '17:00:00', NULL, 4, '2024-01-09'),
    ('Amanda Johnson', '090-123-4567', 5, 'password10', 'amanda.johnson@example.com', '08:30:00', '17:30:00', NULL, 5, '2024-01-10');



INSERT INTO "Isplata" ("ZaposlenikID", "Datum", "Plaća") VALUES
    (1, '2024-01-01 12:00:00', 1),
    (2, '2024-01-02 12:00:00', 2),
    (3, '2024-01-03 12:00:00', 3),
    (4, '2024-01-04 12:00:00', 4),
    (5, '2024-01-05 12:00:00', 5),
    (6, '2024-01-06 12:00:00', 5),
    (7, '2024-01-07 12:00:00', 3),
    (8, '2024-01-08 12:00:00', 1),
    (9, '2024-01-09 12:00:00', 2),
    (10, '2024-01-10 12:00:00', 3);


