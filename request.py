import configuration
def cr_order(order_body):
   return requests.post(configuration.URL_SERVICE + configuration.CR_ORDER,
                         json=order_body)
def get_order_info_by_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_INFORMATION + str(track))