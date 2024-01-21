
DROP TRIGGER IF EXISTS trg_update_vehicle_kilometers ON "WorkLog";
DROP FUNCTION IF EXISTS update_vehicle_kilometers();







DROP TRIGGER IF EXISTS trg_calculate_placa_fields ON "Plaća";
DROP FUNCTION IF EXISTS calculate_placa_fields();



DROP TRIGGER IF EXISTS trg_update_service_dates ON "Vozilo";
DROP FUNCTION IF EXISTS update_service_dates();


DROP TRIGGER IF EXISTS trg_update_registration_dates ON "Vozilo";
DROP FUNCTION IF EXISTS update_registration_dates();


DROP TRIGGER IF EXISTS trg_generate_employee_info ON "Zaposlenik";
DROP FUNCTION IF EXISTS generate_employee_info();



DROP TABLE IF EXISTS "Trošak";
DROP TABLE IF EXISTS "WorkLog";
DROP TABLE IF EXISTS "Isplata";
DROP TABLE IF EXISTS "Zaposlenik";
DROP TABLE IF EXISTS "Radno mjesto";
DROP TABLE IF EXISTS "Plaća";
DROP TABLE IF EXISTS "Status";
DROP TABLE IF EXISTS "Vozilo";
DROP TABLE IF EXISTS "Trošak_Vrsta";


