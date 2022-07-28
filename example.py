import whmcspy

WHMCS_URL = "http://50.3.80.92/includes/api.php"
WHMCS_IDENTIFIER = "lhQSOIW4LeGUxolKWSNb8ZCkTnb5uPsm"
WHMCS_SECRET = "TKOYRUU7yjV409gvhGCzz8aNxK2oWd8F"

domain = "whmcs.test"
whmcs = whmcspy.WHMCS(WHMCS_URL, WHMCS_IDENTIFIER, WHMCS_SECRET)
client = whmcs.add_client(
    firstname="firstname",
    lastname="lastname",
    email="email2@email.com",
    address1="address1",
    city="city",
    state="state",
    postcode=123456,
    country="GB",
    phonenumber=1232131321,
    password2="password2"
)
whmcs.update_client(
    clientid=client,
    firstname="firstname",
    lastname="lastname",   
)
product = {
	"id": whmcs.add_product(name="test", gid=1),
	"domain": domain
}
order = whmcs.add_order(clientid=client, products=[product])
whmcs.cancel_order(order["orderid"])

