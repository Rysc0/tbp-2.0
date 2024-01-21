-- Drop the trigger
DROP TRIGGER IF EXISTS trg_update_vehicle_kilometers ON "WorkLog";

-- Drop the trigger function
DROP FUNCTION IF EXISTS update_vehicle_kilometers();

-- Drop the trigger
DROP TRIGGER IF EXISTS trg_check_placa_constraints ON "Plaća";

-- Drop the trigger function
DROP FUNCTION IF EXISTS check_placa_constraints();



-- Drop the trigger
DROP TRIGGER IF EXISTS trg_calculate_placa_fields ON "Plaća";

-- Drop the trigger function
DROP FUNCTION IF EXISTS calculate_placa_fields();


-- Drop the trigger
DROP TRIGGER IF EXISTS trg_update_service_dates ON "Vozilo";

-- Drop the trigger function
DROP FUNCTION IF EXISTS update_service_dates();




DROP TABLE IF EXISTS "Trošak";
DROP TABLE IF EXISTS "WorkLog";
DROP TABLE IF EXISTS "Isplata";
DROP TABLE IF EXISTS "Zaposlenik";
DROP TABLE IF EXISTS "Radno mjesto";
DROP TABLE IF EXISTS "Plaća";
DROP TABLE IF EXISTS "Status";
DROP TABLE IF EXISTS "Vozilo";
DROP TABLE IF EXISTS "Trošak_Vrsta";


