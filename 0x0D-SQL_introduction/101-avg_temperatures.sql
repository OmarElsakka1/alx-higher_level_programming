-- Getting average temperature in (Fahrenheit) by city order in DESC;
SELECT `city`, AVG(`value`) AS `avg_temp` FROM `temperatures` GROUP BY `city` ORDER BY `avg_temp` DESC;
