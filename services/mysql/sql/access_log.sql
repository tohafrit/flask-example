USE whist;

CREATE TABLE IF NOT EXISTS access_log (
  id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  -- record_date DATE NOT NULL COMMENT 'record date',
  -- record_time TIME NOT NULL COMMENT 'record time',
  visit_count INT NOT NULL COMMENT 'count',
  record_datetime DATETIME(6) NOT NULL COMMENT 'record date',
  client_ip VARCHAR(32) COMMENT 'client ip',
  internal_ip VARCHAR(32) COMMENT 'internal ip'
)
COMMENT 'table with some information';
