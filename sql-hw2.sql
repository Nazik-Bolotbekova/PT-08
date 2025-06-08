INSERT INTO users(id,email,full_name,age,created_at)
VALUES
(5,'belov@site.com','Nikita Belov',24,NOW());

DELETE FROM users
WHERE id = 5;

INSERT INTO jobs(id,title,salary,is_active)
VALUES
(4,'Frontend Developer',120000,true),
(5,'Security analyst',110000,true),
(6,'Project manager',100000,false),
(7,'Backend Developer',125000,false),
(8,'DevOps',130000,true);

INSERT INTO applications(id,user_id,job_id,status,applied_at)
VALUES
(4,2,1,'submitted',NOW());

INSERT INTO users(id,email,full_name,age,created_at)
VALUES
(6,'antropov@gmail.com','Antropov arseniy',28,NOW()),
(7,'artem@apple.com','Koshelev Artem',18,NOW()),
(8,'kovalenco@site.com','Kovalenco Snejana',20,NOW());

INSERT INTO jobs(id,title,salary,is_active)
VALUES
(11,'Full-Stack Developer',125000*1.1,true),
(12,'Project manager',110000*1.1,true);

UPDATE users
SET age = age + 1
WHERE age >= 30;

UPDATE users
SET email = '@protonmail.com'
WHERE email LIKE '%@gmail.com';

UPDATE users
SET full_name = full_name || ' (fired)'
WHERE age >= 50;

UPDATE users
SET full_name = 'Tim Cook' --Получилось не с первого раза--
WHERE id = 3;

UPDATE jobs
SET salary = NULL
WHERE is_active = false;

UPDATE applications
SET status = 'archived'
WHERE  applied_at >= NOW() - INTERVAL '30 days';

ALTER TABLE users ADD status_level TEXT;

UPDATE users
SET status_level = CASE
	WHEN age < 25 THEN 'junior'
	WHEN age >= 25 AND age <= 35 THEN 'middle'
	WHEN age > 35 THEN 'senior'
END;

DELETE FROM users WHERE age < 18;

UPDATE applications
SET status = 'draft'
WHERE id = 1;

DELETE FROM applications WHERE status = 'draft';

DELETE FROM jobs WHERE id NOT IN(SELECT DISTINCT job_id FROM applications);

UPDATE users
SET email = '@artem.ru'
WHERE id = 7;

DELETE FROM users WHERE email LIKE '%.ru';
