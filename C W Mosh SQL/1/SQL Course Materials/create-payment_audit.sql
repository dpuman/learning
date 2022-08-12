use sql_invoicing;

create table payment_audit
(
	client_id INT,
    date DATE,
    ammount DECIMAL(9,2),
    action_type VARCHAR(50),
    action_date DATETIME
)