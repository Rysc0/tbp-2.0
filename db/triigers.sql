CREATE OR REPLACE FUNCTION update_vehicle_kilometrage()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.Vozilo IS NOT NULL AND NEW.Kilometraža IS NOT NULL THEN
        UPDATE "Vozilo"
        SET "Kilometraža" = "Kilometraža" + NEW.Kilometraža
        WHERE "ID" = NEW.Vozilo;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_vehicle_kilometrage_trigger
BEFORE INSERT ON "WorkLog"
FOR EACH ROW
EXECUTE FUNCTION update_vehicle_kilometrage();


CREATE OR REPLACE FUNCTION update_vehicle_kilometers()
RETURNS TRIGGER AS $$
BEGIN
    if NEW.Vozilo != NULL
    then 
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
