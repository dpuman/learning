CREATE OR REPLACE view sales_by_client as
select c.client_id,c.name,sum(invoice_total) as total_sales
from clients c
join invoices i using (client_id)
GROUP BY c.client_id,c.name
order by c.client_id