import whmcspy

WHMCS_URL = "http://whmcs.test/includes/api.php"
WHMCS_IDENTIFIER = "yTJMf0PHFM0ViIAIR9mlfBKnjXzdtcO3"
WHMCS_SECRET = "fAvWuAMWJNY8KBZlHDRhiO4i8bqTPGMb"

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
product = {
	"id": whmcs.add_product(name="test", gid=1),
	"domain": domain
}
order = whmcs.add_order(clientid=1, products=[product])
whmcs.cancel_order(order["orderid"])

