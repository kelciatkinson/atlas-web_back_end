-- Creates an index on the table names and the first letter of name and the score
CREATE INDEX idx_name_first ON names (name(1), score);
