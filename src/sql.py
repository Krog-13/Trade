query_exists = "SELECT order_num, price_us, delivery_time, " \
               "price_rus FROM deliver WHERE num=%s"
query_update = "UPDATE deliver SET order_num=%s, price_us=%s, delivery_time=%s, price_rus=%s WHERE num=%s"
query_add = "INSERT INTO deliver (num, order_num, price_us, delivery_time, price_rus)" \
            " VALUES (%s, %s, %s, %s, %s)"
query_get = "SELECT num, order_num, price_us, delivery_time, " \
               "price_rus FROM deliver"
