-- Lists bands ranked by longevity with Glam rock as main style
SELECT
    band_name,
    (COALESCE(split, 2024) - formed) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
