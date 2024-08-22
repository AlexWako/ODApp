import shopify

# API information for the store
api_key = 
api_version = 

def activate_session(private_app_password):

    # Connects the store
    session = shopify.Session(f"{api_key}:{private_app_password}@okayamadenim.myshopify.com", api_version, private_app_password)

    # Start Session
    shopify.ShopifyResource.activate_session(session)

    try:

         shopify.Product.find_first()

    except:

        return None

    return {
        'X-Shopify-Access-Token': private_app_password,
        'Content-Type': 'application/json'
    }

def close_session():

    # Ends session
    shopify.ShopifyResource.clear_session()

