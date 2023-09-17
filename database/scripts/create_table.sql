CREATE TABLE rdms_accounts (
`id` INT NOT NULL AUTO_INCREMENT,
`name` VARCHAR(64) NOT NULL,
`identity` VARCHAR(256) NOT NULL,
`password` VARCHAR(256) NOT NULL,
`root_permission` BOOLEAN NOT NULL DEFAULT FALSE,
`perference` BLOB,
PRIMARY KEY (id)
)ENGINE=InnoDB CHARSET=utf8mb4;

CREATE TABLE rdms_users (
`id` INT NOT NULL AUTO_INCREMENT,
`name` VARCHAR(64) NOT NULL,
`student_number` INT NOT NULL,
`contacts` VARCHAR(128) NOT NULL,
`note` BLOB,
PRIMARY KEY (id)
)ENGINE=InnoDB CHARSET=utf8mb4;

CREATE TABLE rdms_devices (
`uuid` VARCHAR(36) NOT NULL,
`name` VARCHAR(64) NOT NULL,
`creation_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
`expiration_time` DATETIME,
`is_expired` BOOLEAN,
PRIMARY KEY (uuid)
)ENGINE=InnoDB CHARSET=utf8mb4;

CREATE TABLE rdms_rentals (
`id` INT NOT NULL AUTO_INCREMENT,
`device_uuid` VARCHAR(36) NOT NULL,
`user_id` INT NOT NULL,
`start_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
`end_time` DATETIME,
`is_overdue` BOOLEAN,
`is_returned` BOOLEAN,
PRIMARY KEY (id),
FOREIGN KEY (device_uuid) REFERENCES rdms_devices(uuid),
FOREIGN KEY (user_id) REFERENCES rdms_users(id)
)ENGINE=InnoDB CHARSET=utf8mb4;

CREATE TABLE rdms_audit_logs (
`id` BIGINT NOT NULL AUTO_INCREMENT,
`account_id` INT NOT NULL,
`timestamp` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
`type` TINYINT NOT NULL,
`level` TINYINT NOT NULL,
`text` BLOB,
`data` BLOB,
PRIMARY KEY (id),
FOREIGN KEY (account_id) REFERENCES rdms_accounts(id)
)ENGINE=InnoDB CHARSET=utf8mb4;

CREATE TABLE rdms_device_logs (
`id` BIGINT NOT NULL AUTO_INCREMENT,
`device_uuid` VARCHAR(36) NOT NULL,
`timestamp` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
`type` TINYINT NOT NULL,
`level` TINYINT NOT NULL,
`text` BLOB,
`data` BLOB,
PRIMARY KEY (id),
FOREIGN KEY (device_uuid) REFERENCES rdms_devices(uuid)
)ENGINE=InnoDB CHARSET=utf8mb4;

CREATE TABLE rdms_notification_pool (
`id` INT NOT NULL AUTO_INCREMENT,
`device_uuid` VARCHAR(36) NOT NULL,
`account_id` INT NOT NULL,
`timestamp` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
`title` BLOB NOT NULL,
`contents` BLOB NOT NULL,
`is_pushed` BOOLEAN NOT NULL DEFAULT FALSE,
PRIMARY KEY (id),
FOREIGN KEY (device_uuid) REFERENCES rdms_devices(uuid),
FOREIGN KEY (account_id) REFERENCES rdms_accounts(id)
)ENGINE=InnoDB CHARSET=utf8mb4;