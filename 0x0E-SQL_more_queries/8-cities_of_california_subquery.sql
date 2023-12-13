-- new task sql
SELECT name, id FROM cities WHERE state_id = (SELECT id FROM states WHERE name = "California") ORDER BY id;
