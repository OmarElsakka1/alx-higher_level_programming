-- Grouping all with same score and showing score and its frequency
SELECT `score`, COUNT(*) AS `number` FROM `second_table` GROUP BY `score` ORDER BY `number` DESC;
