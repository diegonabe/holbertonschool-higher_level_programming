-- Muestra la temperatura máxima de cada estado, ordenada por nombre del estado.
SELECT `state`, MAX(`value`) AS `max_temp`
FROM `temperatures`
GROUP BY `state`
ORDER BY `state`;
