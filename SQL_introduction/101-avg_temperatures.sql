-- Muestra la temperatura promedio (en Fahrenheit)
-- por ciudad ordenada por temperatura descendente.
SELECT `city`, AVG(`value`) AS `avg_temp`
FROM `temperatures`
GROUP BY `city`
ORDER BY `avg_temp` DESC;
