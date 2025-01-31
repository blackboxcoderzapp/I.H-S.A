import streamlit as st

st.set_page_config(page_title="The Goated Stall", page_icon="😁", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
    .header {
        text-align: center;
        color: #4CAF50;
        font-size: 50px;
        margin: 20px 0;
    }
    .subheader {
        text-align: center;
        color: #333;
        font-size: 30px;
        margin: 10px 0;
    }
    .tagline {
        text-align: center;
        color: #FF5733;  /* A different color for emphasis */
        font-size: 24px;
        margin: 10px 0;
        font-weight: bold;
    }
    .product {
        border: 1px solid #ddd;
        border-radius: 5px;
        padding: 10px;
        margin: 10px;
        text-align: center;
    }
    .footer {
        text-align: center;
        margin-top: 20px;
        font-size: 20px;
        color: #777;
    }

    /* Style inputs with type="text", select elements and textareas */
input[type=email], select, textarea {
  width: 100%; /* Full width */
  padding: 12px; /* Some padding */ 
  border: 1px solid #ccc; /* Gray border */
  border-radius: 4px; /* Rounded borders */
  box-sizing: border-box; /* Make sure that padding and width stays in place */
  margin-top: 6px; /* Add a top margin */
  margin-bottom: 16px; /* Bottom margin */
  resize: vertical /* Allow the user to vertically resize the textarea (not horizontally) */
}

/* Style the submit button with a specific background color etc */
input[type=submit] {
  background-color: #04AA6D;
  color: white;
  padding: 12px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;


/* When moving the mouse over the submit button, add a darker green color */
input[type=submit]:hover {
  background-color: #45a049;
}
    </style>
""", unsafe_allow_html=True)

# Title of the app
st.markdown('<div class="header">Key Bites & Delight</div>', unsafe_allow_html=True)

# Subheader
st.markdown('<div class="subheader">Delicious Treats and Unique Souvenirs!</div>', unsafe_allow_html=True)

# Tagline
st.markdown('<div class="tagline">Our services are faster than human reaction!</div>', unsafe_allow_html=True)

# Product Data
products = [
    {
        "name": "Pani Puri",
        "image": "https://th.bing.com/th/id/OIP.YDOsXH7xXitC8_4SUDa4OwHaFS?rs=1&pid=ImgDetMain",
        "description": "Enjoy our crispy and spicy Pani Puri!"
    },
    {
        "name": "Shots",
        "image": "https://th.bing.com/th/id/OIP.pxuJBK9nXfnbL-ubq2w-1QHaE8?rs=1&pid=ImgDetMain",
        "description": "Refreshing shots to quench your thirst!"
    },
    {
        "name": "Sports Key Chain",
        "image": "https://down-my.img.susercontent.com/file/sg-11134202-7rd55-lvvxwqbcgk4j88",
        "description": "Grab your favorite sports key chain!"
    }
]

# Display Products
for product in products:
    # Create a container for each product
    with st.container():
        st.markdown(f'<div class="product"><h3>{product["name"]}</h3>', unsafe_allow_html=True)
        st.image(product["image"], use_container_width=True)
        st.markdown(f'<p>{product["description"]}</p></div>', unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">Visit us at the Business Fair!</div>', unsafe_allow_html=True)

contact_form = """
<input type="hidden" name="_captcha" value="false">
<form action="https://formsubmit.co/s.kirtan.bhattar@fountainheadschools.org" method="POST" >
 <input type="text" name="name" placeholder="your name" required >
 <input type="email" name="email" placeholder="your email" required >
 <textarea name="message" placeholder="you may write your message over here" required ></textarea>
 <button type="submit" >Send</button >
</form>      
               
"""
