import Product from "./components/product.js";

const vivo = new Product(
    2,
    "vivo-Y72-5G-8-128-Black",
    "./components/contents/vivo.jpg",
    "The Vivo Y72 smartphone comes with a waterdrop notch for the selfie camera, triple cameras at the back arranged in a rectangular module, a side-mounted fingerprint sensor for security, and a glossy gradient design.",
);

const vivoProd = [vivo];
console.log(vivoProd)

async function fetchProductData(product) {
  const API_ENDPOINT = `http://127.0.0.1:5000/shopify/1/${encodeURIComponent(
    product.name
  )}/500007`;

  try {
    const response = await fetch(API_ENDPOINT);
    if (response.ok) {
      const data = await response.json();
      return { product, data };
    } else {
      console.error("Request failed. Status:", response.status);
      return { product, data: null };
    }
  } catch (error) {
    console.error("Request failed:", error);
    return { product, data: null };
  }
}

const productList = vivoProd.map(async (product) => {
  const { product: productData, data } = await fetchProductData(product);

  let productArticle = document.createElement("article");
  productArticle.classList.add("items-alignment");
  productArticle.setAttribute("id", productData.id);

  if (data && data.length > 0) {
    const dates = data.map((item) => item.date).join(", ");
    const timeslots = data.map((item) => item.timeslots).join(", ");

    productArticle.innerHTML = `
      <figure class="product-image">
        <img src=${productData.image} alt="product-image" loading="lazy" height="300px"/>
      </figure>
      <div class="product-details-container">
        <div class="product-name-container">
          <h1 class="product-name">${productData.name}</h1>
        </div>
        <div class="product-details-list-container">
          <ul class="product-details-list">
            <li class="information">${productData.information}</li>
            <li class="available-dates"><span>Available Dates: </span>${dates}</li>
            <li class="timeslots"><span>Timeslots: </span>${timeslots}</li>
          </ul>
        </div>
      </div>
    `;
  } else {
    productArticle.innerHTML = `
      <div class="error-message">Failed to fetch data for ${productData.name}</div>
    `;
  }

  return productArticle; // Return the dynamically created element
});

const productContainer = document.querySelector(".item-details-container");

Promise.all(productList).then((articles) => {
  articles.forEach((article) => {
    productContainer.appendChild(article);
  });
});

