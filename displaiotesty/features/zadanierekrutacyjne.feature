Feature: Należy napisać test automatyczny, który doda produkt do koszyka oraz wykona kilka sprawdzeń
1. Wejść na stronę główna displate.com.
2. Przejść na jeden z produktów znajdujących się na stronie głównej.
3. Kliknąć w przycisk ‘Select finish & add frame’ i wybrać jedną z ramek.
4. Dodać produkt do koszyka.
5. Przejść do koszyka.
6. Sprawdzić czy został dodany produkt wraz z właściwą ceną.
7. Zmienić kraj na ‘United States’
8. Dodać kod rabatowy znajdujący się na górnej belce strony.
9. Zweryfikować czy cena została poprawnie obliczona po rabacie.

Scenario: customer track for usa with discount
	Given we start at homepage
	When we click at first product
	Then we should land on product page
	When we select product frame
	And we select product finish
	And we add product to cart
	Then we should proceed to cart
	And we should land on cart page
	And we should check if price is fine
	When we change country to united states
	Then we should see proper country
	When we use promo code from topbar
	Then we should see price has changed 