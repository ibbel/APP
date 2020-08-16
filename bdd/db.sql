use users;
CREATE TABLE users(
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, 
    nom VARCHAR(45),
    prenom VARCHAR(45),
    naissance VARCHAR(45),
    mail VARCHAR(100),
    login VARCHAR(45),
    password VARCHAR(45)
);