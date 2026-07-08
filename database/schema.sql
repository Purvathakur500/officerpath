CREATE TABLE IF NOT EXISTS Users (
    user_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    target_exam VARCHAR(20) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS StudySessions (
    session_id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    subject VARCHAR(100) NOT NULL,
    task_type VARCHAR(100) NOT NULL,
    duration_minutes INTEGER NOT NULL,
    study_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id)
    REFERENCES Users(user_id)
);
CREATE TABLE IF NOT EXISTS MockResults (
    result_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES Users(user_id),
    subject VARCHAR(50),
    score INTEGER,
    total_questions INTEGER,
    percentage DECIMAL(5,2),
    test_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE PYQResults (
    result_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES Users(user_id),
    exam VARCHAR(50),
    score INTEGER,
    total_questions INTEGER,
    percentage DECIMAL(5,2),
    test_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);