create database email_sender;

\c email_sender

create table emails (
  id serial not null,
  data timestamp not null default current_timestamp,
  asunto varchar(100) not null,
  message varchar(255) not null
);