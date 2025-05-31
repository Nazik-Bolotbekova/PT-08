CREATE TYPE gender_enum AS ENUM('male','female','other') --Создаем тип енам--
CREATE TABLE students(   --Создаем табличку--
	"id" SERIAL PRIMARY KEY,  --Уникальный и последовательный id ключ--
	"full_name" VARCHAR(100) NOT NULL, --Обязательное поле с ограничением до 100 символов--
	"age" INT CHECK (age > 5 AND age < 100), --Поле для возраста студента с ограничением--
	"email" VARCHAR(255) UNIQUE, --Уникальное поле email с ограничением до 255 символов--
	"grade" NUMERIC(4,1), --Тип данных NUMERIC число до 4 и 1 после запятой--
	"is_active" BOOLEAN DEFAULT TRUE, --Логическое знчение BOOLEAN, по умолчанию TRUE--
	"gender" gender_enum, --Тип енам с тремя возможными значениями--
	"enrolled_at" DATE DEFAULT CURRENT_DATE --Поле даты зачисления, по умолчанию будет использоваться сегодняшняя дата--
);

DROP TABLE students; --Сбрасываем табличку при необходимости--

ALTER TABLE students ADD COLUMN parent_contact TEXT; --Создаем колонку parent_contact с типом TEXT--

ALTER TABLE students RENAME COLUMN grade TO average_grade; --Переименуем колонку grade на average_grade--

ALTER TABLE students DROP COLUMN parent_contact; --Сбрасываем колонку parent_contact--

ALTER TABLE students ADD COLUMN student_uuid UUID DEFAULT gen_random_uuid(); --Создаем колонку student_uuid с автоматическим значением по умолчанию--
