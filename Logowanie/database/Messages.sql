CREATE TABLE Messages (
  id INT NOT NULL AUTO_INCREMENT,
  user_id INT NOT NULL,
  from_id INT,
  to_id INT,
  mtext TEXT,
  creation_date DATE,
  PRIMARY KEY(id),
  FOREIGN KEY(user_id) REFERENCES Users(id) ON DELETE CASCADE

);
