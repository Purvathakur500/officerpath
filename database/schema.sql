CREATE TABLE Users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    target_exam TEXT NOT NULL,
    created_at DATE DEFAULT CURRENT_DATE
);

CREATE TABLE StudySessions (
    session_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    subject TEXT NOT NULL,
    task_type TEXT NOT NULL,
    duration_minutes INTEGER NOT NULL,
    status TEXT NOT NULL,
    study_date DATE DEFAULT CURRENT_DATE,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);