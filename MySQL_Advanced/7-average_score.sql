-- Creates stored procedure that computes and store average score for student
DELIMITER $$

DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
CREATE procedure ComputeAverageScoreForUser(
    IN user_id INT
)

BEGIN
    DECLARE average_score FLOAT;
    SELECT AVG(score) INTO average_score FROM corrections WHERE corrections.user_id = user_id;

    UPDATE users
    SET average_score = average_score
    WHERE id = user_id;
END$$
DELIMITER ;
