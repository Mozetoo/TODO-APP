
document.addEventListener('DOMContentLoaded', function() {
    const changingText = document.getElementById('changingText');

    setInterval(function() {
        if (changingText.textContent === 'Get Things Done') {
            changingText.textContent = 'Master Your Time';
        } else {
            changingText.textContent = 'Get Things Done';
        }
    }, 3000); // Change the word every 3 seconds (3000 milliseconds)
});

document.addEventListener('DOMContentLoaded', function() {
    const changingImage = document.getElementById('changingImage');
    let currentIndex = 0;

    changingImage.src = imageUrls[currentIndex]; // Set initial image before starting the interval

    setInterval(function() {
        currentIndex = (currentIndex + 1) % imageUrls.length;
        changingImage.src = imageUrls[currentIndex];
    }, 3000); // Change the image every 3 seconds (3000 milliseconds)
});

document.addEventListener('DOMContentLoaded', function() {
    const features = document.querySelectorAll('.feature');

    // Function to check if an element is in the viewport
    function isElementInViewport(el) {
        const rect = el.getBoundingClientRect();
        return (
            rect.top >= 0 &&
            rect.left >= 0 &&
            rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
            rect.right <= (window.innerWidth || document.documentElement.clientWidth)
        );
    }

    function animateElements() {
        features.forEach(feature => {
            if (isElementInViewport(feature)) {
                feature.classList.add('show');
            }
        });
    }

    // Call the animateElements function on page load and scroll
    animateElements();
    window.addEventListener('scroll', animateElements);
});

function isElementInViewport(el) {
    var rect = el.getBoundingClientRect();
    return (
        rect.top >= 0 &&
        rect.left >= 0 &&
        rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
}

// Function to handle the scroll event and trigger animations
function handleScroll() {
    var textDiv = document.querySelector(".text-animate-left");
    var imageDiv = document.querySelector(".image-animate-right");

    if (isElementInViewport(textDiv)) {
        textDiv.classList.add("animate-in");
    }

    if (isElementInViewport(imageDiv)) {
        imageDiv.classList.add("animate-in");
    }
}

// Attach the handleScroll function to the scroll event
window.addEventListener("scroll", handleScroll);

 $(document).ready(function () {
        $('.nav-item-clickable').on('click', function () {
            // Remove the 'active' class from all links
            $('.nav-link').removeClass('active');

            // Add the 'active' class to the clicked link
            $(this).find('.nav-link').addClass('active');
        });
    });

