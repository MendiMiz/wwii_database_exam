explain analyze
select count(m.air_force), m.air_force, m.target_city
from mission as m
where extract(year from mission_date) = 1943
GROUP BY m.air_force, m.target_city
order by count(m.air_force) desc limit 1
Execution Time: 60.476 ms


explain analyze
select bomb_damage_assessment, count(target_country) from mission
where bomb_damage_assessment is not null
and airborne_aircraft > 5
group by target_country, bomb_damage_assessment
order by count(bomb_damage_assessment) desc limit 1
Execution Time: 40.338 ms

יוצר אינדקסים לעמודות שהשתמשנו בחיפוש
air_force, target_city, target_country, bomb_damage_assessment


CREATE INDEX idx_air_force ON mission (air_force);
CREATE INDEX idx_target_city ON mission (target_city);
CREATE INDEX idx_target_country ON mission (target_country);
CREATE INDEX idx_bomb_damage_assessment ON mission (bomb_damage_assessment);
CREATE INDEX idx_mission_date ON mission (mission_date);


explain analyze
select count(m.air_force), m.air_force, m.target_city
from mission as m
where extract(year from mission_date) = 1943
GROUP BY m.air_force, m.target_city
order by count(m.air_force) desc limit 1
Execution Time: 0.256 ms


explain analyze
select bomb_damage_assessment, count(target_country) from mission
where bomb_damage_assessment is not null
and airborne_aircraft > 5
group by target_country, bomb_damage_assessment
order by count(bomb_damage_assessment) desc limit 1
Execution Time: 0.130 ms

