SQL = """SELECT d.department_id, 
                d.department_name, 
                e.first_name 
         FROM departments d 
            INNER JOIN employees e 
            ON d.department_id = e.department_id
         ORDER BY first_name"""