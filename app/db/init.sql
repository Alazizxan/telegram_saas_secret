CREATE TABLE bots (
    id SERIAL PRIMARY KEY,
    owner_id INTEGER,
    token TEXT,
    is_active BOOLEAN DEFAULT TRUE
);

CREATE TABLE bot_texts (
    id SERIAL PRIMARY KEY,
    bot_id INTEGER,
    key TEXT,
    text TEXT
);

CREATE TABLE sessions (
    id SERIAL PRIMARY KEY,
    bot_id INTEGER,
    user_id BIGINT,
    path TEXT
);
