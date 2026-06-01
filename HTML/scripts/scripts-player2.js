let imagesPath, imagePrefix, totalImages;
let currentImageIndex = 1;
let animationInterval = null;
let animationSpeed = 200;
let controlsVisible = true;

function initialize() {
  // Obtener rutas de imágenes desde el HTML
  const imageConfig = document.getElementById("image-config");
  imagesPath = imageConfig.getAttribute("data-images-path");
  imagePrefix = imageConfig.getAttribute("data-image-prefix");
  totalImages = parseInt(imageConfig.getAttribute("data-total-images"), 10);

  preloadImages();
  updateImage();
  playAnimation();
  setupAutoHideControls(); // Configurar la aparición y desaparición de los controles
  setupKeyboardControls(); // Configurar los controles del teclado
}

function setupAutoHideControls() {
  const controls = document.querySelector("aside.controls");
  const main = document.querySelector("main");

  // Mostrar controles cuando el mouse entra al área de visualización
  document.body.addEventListener("mousemove", () => {
    showControls(controls);
  });

  // Ocultar controles automáticamente después de 1 segundo sin interacción
  let hideTimeout;
  document.body.addEventListener("mousemove", () => {
    clearTimeout(hideTimeout);
    hideTimeout = setTimeout(() => {
      hideControls(controls);
    }, 1000);
  });
}

function hideControls(controls) {
  controls.style.transform = "translateX(-100%)"; // Mover controles fuera de la vista
  expandAnimationArea(); // Expandir el área de animación
  controlsVisible = false;
}

function showControls(controls) {
  controls.style.transform = "translateX(0)"; // Mostrar controles
  restoreAnimationArea(); // Restaurar el área de animación
  controlsVisible = true;
}

function expandAnimationArea() {
  const main = document.querySelector("main");
  const img = document.getElementById("mainImage");
  main.style.marginLeft = "0"; // Elimina el margen izquierdo
  img.style.width = "100vw"; // La imagen ocupa todo el ancho de la ventana
  img.style.height = "100vh"; // La imagen ocupa todo el alto de la ventana
  img.style.objectFit = "contain"; // Mantiene la relación de aspecto
}

function restoreAnimationArea() {
  const main = document.querySelector("main");
  const img = document.getElementById("mainImage");
  main.style.marginLeft = "200px"; // Restaura el margen para los controles
  img.style.width = "calc(100vw - 200px)"; // Ajusta el ancho según el margen
  img.style.height = "100vh"; // Mantiene el alto de la ventana
  img.style.objectFit = "contain"; // Mantiene la relación de aspecto
}

function preloadImages() {
  for (let i = 1; i <= totalImages; i++) {
    const img = new Image();
    img.src = `${imagesPath}${imagePrefix}${i}.webp`;
  }
}

function playAnimation() {
  stopAnimation();
  animationInterval = setInterval(() => {
    nextImage();
  }, animationSpeed);
}

function stopAnimation() {
  clearInterval(animationInterval);
  animationInterval = null;
}

function nextImage() {
  currentImageIndex = (currentImageIndex % totalImages) + 1;
  updateImage();
}

function prevImage() {
  currentImageIndex = (currentImageIndex - 2 + totalImages) % totalImages + 1;
  updateImage();
}

function updateImage() {
  const img = document.getElementById("mainImage");
  const imageCounter = document.getElementById("imageCounter");
  img.src = `${imagesPath}${imagePrefix}${currentImageIndex}.webp`;
  if (imageCounter) {
    imageCounter.textContent = `Imagen ${currentImageIndex} de ${totalImages}`;
  }
}

function changeSpeed(delta) {
  animationSpeed = Math.max(50, animationSpeed + delta);
  if (animationInterval) {
    playAnimation();
  }
}

function setupKeyboardControls() {
  document.addEventListener("keydown", (event) => {
    if (event.key === "ArrowRight") {
      nextImage();
    } else if (event.key === "ArrowLeft") {
      prevImage();
    } else if (event.key === " ") {
      event.preventDefault(); // Evita el desplazamiento con la barra espaciadora
      if (animationInterval) {
        stopAnimation();
      } else {
        playAnimation();
      }
    }
  });
}

// Recargar la página automáticamente cada 5 minutos
function setupAutoReload() {
  const reloadInterval = 5 * 60 * 1000; // 5 minutos en milisegundos
  setInterval(() => {
    location.reload(); // Recarga la página completa
  }, reloadInterval);
}

// Llama a setupAutoReload dentro de initialize
function initialize() {
  const imageConfig = document.getElementById("image-config");
  imagesPath = imageConfig.getAttribute("data-images-path");
  imagePrefix = imageConfig.getAttribute("data-image-prefix");
  totalImages = parseInt(imageConfig.getAttribute("data-total-images"), 10);

  if (!imagesPath || !imagePrefix || !totalImages) {
    console.error("Error: Las rutas de las imágenes no están configuradas correctamente.");
    return;
  }

  preloadImages();
  updateImage();
  playAnimation();
  setupAutoHideControls(); // Configurar la aparición y desaparición de los controles
  setupAutoReload(); // Activar recarga automática
  setupKeyboardControls(); // Configurar los controles del teclado
}
