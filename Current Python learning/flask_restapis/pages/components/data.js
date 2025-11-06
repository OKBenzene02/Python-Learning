import Product from "./product.js";

const apple = new Product(
    1,
    "Apple_iPhone_14 Pro Max_512GB_Gold",
    "./components/contents/apple-14.jpg",
    "The iPhone 14 and iPhone 14 Plus (also stylized as iPhone 14+) are smartphones designed, developed, and marketed by Apple Inc.",
);

const products = [apple];
console.log(products);

export default products;