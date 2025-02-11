-- Lists bands ranked by longevity with Glam rock as main style
SELECT
    band_name,
    COALESCE(YEAR(split), YEAR(CURDATE())) - formed as lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
