import streamlit as st
import random
import pandas as pd

if "memory" not in st.session_state:
    st.session_state.memory = []

if "lucky_dish" not in st.session_state:
    st.session_state.lucky_dish = None

# Sample Data
data = {
    'Dish': [
        'Maafe', 'Pounded Yam and Egusi Soup', 'Samp', 'Callaloo', 'Fried Plantains', 'Couscous',
        'Chinchinga', 'Pepper Soup', 'Sobo', 'Jollof Rice with Fried Plantains', 'Bammy', 'Acarajé',
        'Gari Fortor', 'Bitter Kola', 'Fried Fish and Banku', 'Mofongo', 'Shakshuka', 'Chapman',
        'Yam Porridge', 'Eba and Okra Soup', 'Kedjenou', 'Nkwobi', 'Pistache', 'Gumbo', 'Khoresht Fesenjan',
        'Chakhokhbili', 'Bubur Ayam', 'Gallo Pinto', 'Tamales de Elote', 'Kachkán', 'Khachapuri', 'Sauerbraten','Jollof Rice', 'Bunny Chow', 'Biltong', 'Bitterleaf Soup', 'Pap and Wors', 'Fufu', 
        'Egusi Soup', 'Griot', 'Curry Goat', 'Samosa', 'Jerk Chicken', 'Baja Soup', 'Mafe', 
        'Shiro', 'Piri Piri Chicken', 'Chakalaka', 'Yassa Chicken', 'Sundubu Jjigae', 
        'Red Red', 'Suya', 'Kelewele'
    ],
    'Cuisine': [
        'West African', 'Nigerian', 'South African', 'Caribbean', 'Africa, Caribbean, Latin America', 'North African',
        'Ghanaian', 'West African', 'West African', 'Nigerian', 'Jamaican', 'Brazilian',
        'Ghanaian', 'Nigerian', 'Ghanaian', 'Puerto Rican', 'North African, Middle Eastern', 'Nigerian',
        'Nigerian', 'Nigerian', 'Ivory Coast', 'Nigerian', 'Haitian', 'U.S. Gulf Coast', 'Persian',
        'Georgian', 'Indonesian', 'Costa Rican, Nicaraguan', 'Mexican', 'Kazakh', 'Georgian', 'German','West African', 'South African', 'South African', 'Nigerian', 'South African', 'West and Central African', 
        'Nigerian', 'Haitian', 'Caribbean', 'African, South Asian', 'Jamaican', 'Kenyan', 'West African', 
        'Ethiopian', 'Mozambican', 'South African', 'Senegalese', 'South African', 'Ghanaian', 'Nigerian', 'Ghanaian'
    ],
    'Flavor': [
        'Savory, Peanut-rich, Spicy', 'Earthy, Savory, Nutty', 'Soft, Mild, Corny', 'Vegetal, Savory, Sweet', 
        'Sweet, Crispy, Savory', 'Mild, Savory, Grainy', 'Spicy, Savory, Smoky', 'Spicy, Brothy, Bold', 
        'Sweet, Tangy, Refreshing', 'Savory, Tangy, Spicy', 'Mild, Soft, Sweet', 'Spicy, Savory, Crispy', 
        'Savory, Spicy, Starchy', 'Bitter, Woody', 'Savory, Spicy, Rich', 'Garlicky, Savory, Rich', 
        'Spicy, Tangy, Savory', 'Sweet, Citrusy, Fruity', 'Savory, Spicy, Hearty', 'Savory, Slimy, Spicy', 
        'Savory, Spicy, Aromatic', 'Spicy, Creamy, Meaty', 'Sweet, Nutty, Spicy', 'Savory, Spicy, Rich', 
        'Tangy, Sweet, Savory', 'Herby, Savory, Tomato-rich', 'Savory, Spicy, Comforting', 'Savory, Mild, Hearty', 
        'Sweet, Corny, Spicy', 'Savory, Meaty, Fermented', 'Cheesy, Savory, Eggy', 'Tangy, Savory, Rich','Savory, Spicy, Tomato-rich', 'Spicy, Savory, Bread-based', 'Savory, Smoky, Meaty', 'Bitter, Spicy, Savory', 
        'Savory, Hearty, Meat-based', 'Starchy, Mild, Savory', 'Nutty, Savory, Spicy', 'Savory, Fried, Pork-rich',
        'Spicy, Savory, Meat-based', 'Spicy, Savory, Fried', 'Spicy, Savory, Grilled', 'Savory, Beefy, Tomato-based',
        'Savory, Peanut-rich, Stewy', 'Spicy, Chickpea, Savory', 'Spicy, Garlic-rich, Chicken-based', 'Savory, Spicy, Relish',
        'Tangy, Savory, Chicken-based', 'Spicy, Stewy, Soft Tofu', 'Savory, Hearty, Bean-based', 'Spicy, Meaty, Skewered',
        'Spicy, Fried, Plantain-based'
    ],
    'Tags': [
        ['Meat', 'Peanut-rich', 'Stew'], ['Starchy', 'Spicy', 'Nutty'], ['Soft', 'Corny', 'Hearty'],
        ['Vegetal', 'Crab', 'Savory'], ['Fried', 'Sweet', 'Snack'], ['Grain', 'Stew', 'Vegetable'],
        ['Grilled', 'Spicy', 'Skewered'], ['Spicy', 'Broth', 'Meat'], ['Sweet', 'Refreshing', 'Beverage'],
        ['Rice', 'Savory', 'Fried'], ['Flatbread', 'Savory', 'Side'], ['Fried', 'Savory', 'Peanut'],
        ['Fermented', 'Spicy', 'Starchy'], ['Bitter', 'Snack', 'Medicinal'], ['Grilled', 'Savory', 'Stew'],
        ['Fried', 'Comfort Food', 'Hearty'], ['Poached', 'Savory', 'Tangy'], ['Cocktail', 'Citrus', 'Spicy'],
        ['Spicy', 'Hearty', 'Tomato'], ['Starchy', 'Vegetable', 'Hearty'], ['Stew', 'Spicy', 'Meat'],
        ['Savory', 'Meat', 'Fermented'], ['Nutty', 'Sweet', 'Spicy'], ['Stew', 'Meat', 'Rich'],
        ['Tangy', 'Savory', 'Nutty'], ['Stew', 'Spicy', 'Aromatic'], ['Savory', 'Soup', 'Comforting'],
        ['Rice', 'Vegetable', 'Hearty'], ['Sweet', 'Corn', 'Spicy'], ['Meat', 'Savory', 'Fermented'],
        ['Cheese', 'Bread', 'Savory'], ['Pot Roast', 'Slow Cooked', 'Savory'],  ['Rice', 'Tomato', 'Spicy'], ['Bread', 'Curry', 'Savory'], ['Dried', 'Meat', 'Savory'], 
        ['Bitter', 'Soup', 'Meat'], ['Starchy', 'Sausage', 'Hearty'], ['Starchy', 'Smooth', 'Savory'], 
        ['Soup', 'Nutty', 'Hearty'], ['Pork', 'Fried', 'Spicy'], ['Meat', 'Spicy', 'Slow Cooked'], 
        ['Pastry', 'Fried', 'Savory'], ['Grilled', 'Spicy', 'Chicken'], ['Beef', 'Tomato', 'Savory'], 
        ['Peanut', 'Stew', 'Savory'], ['Chickpea', 'Spicy', 'Vegetarian'], ['Chicken', 'Spicy', 'Grilled'], 
        ['Vegetable', 'Spicy', 'Side'], ['Chicken', 'Tangy', 'Marinated'], ['Tofu', 'Spicy', 'Stew'], 
        ['Beans', 'Savory', 'Hearty'], ['Skewered', 'Spicy', 'Meat'], ['Plantain', 'Spicy', 'Snack']
    ],
    'links':[
        'https://www.africanbites.com/maafe-west-african-peanut-soup/',
        'https://cookpad.com/ng/recipes/16461627-pounded-yam-with-egusi-soup',
        'https://www.spar.co.za/recipes/view/savoury-samp',
        'https://thatgirlcookshealthy.com/jamaican-callaloo/',
        'https://www.butterbeready.com/fried-sweet-plantains-recipe/',
        'https://www.loveandlemons.com/how-to-cook-couscous/',
        'https://veganbangla.com/2020/07/17/chichinga-bhaji-snake-gourd-stir-fry/',
        'https://www.allrecipes.com/recipe/13263/rainbow-roasted-pepper-soup/',
        'https://nationalpost.com/life/food/recipes-together-at-sobo-lisa-ahier',
        'https://www.foodnetwork.com/fnk/recipes/joloff-rice-with-fried-plantains-8145274',
        'https://thatgirlcookshealthy.com/jamaican-bammy-recipe/',
        'https://www.thespruceeats.com/brazilian-black-eyed-pea-shrimp-fritters-3028859',
        'https://gingerandseasalt.com/gari-foto/',
        'https://myexoticfruit.com/shop/#!/products/bitter-kola',
        'https://panlasangpinoy.com/filipino-food-fried-fish-tilapia-dish/',
        'https://www.allrecipes.com/recipe/217985/mofongo/',
        'https://downshiftology.com/recipes/shakshuka/',
        'https://www.yummymedley.com/nigerias-favorite-mocktail-chapman/',
        'https://www.myactivekitchen.com/asaro-elepo-rederede-yam-porridge/',
        'https://cookpad.com/ng/recipes/13860209-eba-okro-soup-stew',
        'https://www.africanbites.com/kedjenou-chicken/',
        'https://www.mydiasporakitchen.com/nkwobi-nigerian-cow-foot-special/',
        'https://www.sweetandsavorybyshinee.com/homemade-pistachio-paste/',
        'https://www.allrecipes.com/recipe/216888/good-new-orleans-creole-gumbo/',
        'https://persianmama.com/chicken-in-walnut-pomegranate-sauce-khoresht-fesenjan/',
        'https://nofrillskitchen.com/chakhokhbili-recipe/',
        'https://dailycookingquest.com/bubur-ayam-chicken-congee.html',
        'https://stripedspatula.com/gallo-pinto/',
        'https://www.isabeleats.com/tamales-de-elote/',
        'https://bottomofthepot.com/homemade-kashk/',
        'https://simplyhomecooked.com/khachapuri-georgian-cheese-bread/',
        'https://www.allrecipes.com/recipe/221361/traditional-sauerbraten/',
        'https://www.allrecipes.com/chef-johns-jollof-rice-recipe-7499757',
        'https://www.africanbites.com/bunny-chow/',
        'https://www.greedyferret.com/perfect-biltong-recipe-south-african-beef-jerky',
        'https://allnigerianfoods.com/nigerian-bitterleaf-soup/',
        'https://melissamayo.com/recipe/mielie-pap-gravy-boerewors/',
        'https://cheflolaskitchen.com/fufu-recipe-how-to-make-fufu/',
        'https://www.allrecipes.com/recipe/12978/egusi-soup/',
        'https://foreignfork.com/haitian-griot-recipe/',
        'https://www.africanbites.com/jamaican-curry-goat/',
        'https://www.indianhealthyrecipes.com/samosa-recipe-make-samosa/',
        'https://www.lecremedelacrumb.com/baja-chicken-soup/',
        'https://www.lecremedelacrumb.com/baja-chicken-soup/',
        'https://lowcarbafrica.com/mafe-senegalese-peanut-stew/',
        'https://urbanfarmie.com/shiro-wat/',
        'https://www.allrecipes.com/peri-peri-chicken-recipe-7507145',
        'https://www.africanbites.com/chakalaka/',
        'https://www.seriouseats.com/chicken-yassa-senegalese-braised-chicken-with-caramelized-onions-5215703',
        'https://www.maangchi.com/recipe/sundubu-jjigae ',
        'https://www.africanbites.com/red-redafrican-stewed-black-eyed-peas/',
        'https://www.africanbites.com/suyaspicy-grilled-kebab/',
        'https://travelandmunchies.com/kelewele/'
        ]
}

df = pd.DataFrame(data)

# Function to suggest food
def suggest_food(user_input):
    user_input = user_input.strip().lower()
    if not user_input:
        return "Please enter a valid food name, tag, or country."

    # Match exact dish name
    matching_dish = df[df['Dish'].str.lower() == user_input]
    if not matching_dish.empty:
        return matching_dish[['Dish', 'Cuisine', 'Tags']]

    # Match dishes that contain the tag
    matching_tag_dishes = df[df['Tags'].apply(lambda tags: any(user_input in tag.lower() for tag in tags))]
    if not matching_tag_dishes.empty:
        matching_tag_dishes['Tags'] = matching_tag_dishes['Tags'].apply(lambda x: ', '.join(x))
        return matching_tag_dishes[['Dish', 'Cuisine', 'Tags']]

    # Match dishes based on cuisine
    matching_cuisine_dishes = df[df['Cuisine'].str.lower().str.contains(user_input)]
    if not matching_cuisine_dishes.empty:
        matching_cuisine_dishes['Tags'] = matching_cuisine_dishes['Tags'].apply(lambda x: ', '.join(x))
        return matching_cuisine_dishes[['Dish', 'Cuisine', 'Tags']]

    return "No matching dishes, tags, or cuisines found. Please try another input."

# Title
st.title("SoulBite")

# Sidebar Navigation
st.sidebar.title("Bitefile")
page = st.sidebar.radio("Navigator", ["Home Page", "About SoulBite", "Settings & Memories"])

# Home Page
if page == "Home Page":
    st.subheader("Explore food here")
    st.write("Input a dish name, cuisine, or tag to get food suggestions!")

    # "I'm Feeling Lucky" Button
    if st.button("I'm Feeling Lucky 🎲"):
        random_index = random.choice(df.index)
        st.session_state.lucky_dish = df.loc[random_index]

    # Display Lucky Dish
# Display Lucky Dish
    if st.session_state.lucky_dish is not None:
        index = df[df["Dish"] == st.session_state.lucky_dish["Dish"]].index[0]
        dish_link = df.loc[index, "links"]  # Fetch the corresponding link
    
        with st.container():
            st.markdown(
                f"""
                <div style="height: 200px; border: 2px solid #171717; padding: 10px;
                border-radius: 10px; background-color: #0E0E0E; text-align: center;">
                    <h1>{st.session_state.lucky_dish["Dish"]}</h1>
                    <p><b>Cuisine:</b> {st.session_state.lucky_dish["Cuisine"]}</p>
                    <a href="{dish_link}" target="_blank" style="color: #FFA500; font-size: 18px;">
                        🔗 View Recipe
                    </a>
                </div>
                """,
                unsafe_allow_html=True
            )
    # Chatbox
    userPrompt = st.chat_input("Search for a dish, cuisine, or tag:")

    if userPrompt:
        results = suggest_food(userPrompt)

        # Container thing
        with st.container():
            st.markdown(
                """
                <style>
                    .food-container {
                        height: 200px;
                        border: 2px solid #171717;
                        padding: 10px;
                        border-radius: 10px;
                        background-color: #0E0E0E;
                        text-align: center;
                        overflow-y: auto;
                    }
                </style>
                """,
                unsafe_allow_html=True
            )

            if isinstance(results, str):
                st.markdown(f'<div class="food-container"><h3>{results}</h3></div>', unsafe_allow_html=True)
            else:
                for index, row in results.iterrows():
                    dish_link = df.loc[index, "links"]  # Fetch corresponding link
        
                    st.markdown(
                        f"""
                        <div class="food-container">
                            <h1>{row["Dish"]}</h1>
                            <p><b>Cuisine:</b> {row["Cuisine"]}</p>
                            <a href="{dish_link}" target="_blank" style="color: #FFA500; font-size: 18px;">
                                🔗 View Recipe
                            </a>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

        # Store search history in memory
        st.session_state.memory.append(userPrompt)

elif page == "About SoulBite":
    st.subheader("What is Soulbite?")
    st.write("""SoulBite personalizes dishes from different cultures based on the users pre-existing taste,
    allowing users to easily integrate different cultural cuisines into their daily pallet.
    This enables users to bridge the gap from underrepresented cultural cuisines,
    such as the rich culinary traditions of the Black community.

    Try the Feeling Lucky button to get a random dish!
    """)

# Settings & Memories Page
elif page == "Settings & Memories":
    st.subheader("Your Memories")

    with st.container():
        if st.session_state.memory:
            st.write("Previous Searches:")
            st.write(", ".join(st.session_state.memory))
        else:
            st.write("No memories yet.")

    # Clear search history
    if st.button("Clear Memories"):
        st.session_state.memory = []
        st.success("Memories cleared!")