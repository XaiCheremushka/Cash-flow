document.addEventListener('DOMContentLoaded', function () {
    initDependentFields();
});

function initDependentFields() {
    const typeField = document.querySelector("#id_type");
    const categoryField = document.querySelector("#id_category");
    const subcategoryField = document.querySelector("#id_subcategory");
    const loader = new FullscreenLoader();

    // Функция для загрузки данных с API
    async function loadOptions(url, targetField, dataKey) {
        if (!url) return;

        loader.show();

        try {
            const response = await fetch(url, {
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]").value,
                }
            });

            if (!response.ok) {
                const errorData = await response.json().catch(() => ({}));
                throw new Error(errorData.detail || errorData.message || `HTTP error! status: ${response.status}`);
            }

            const data = await response.json();

            // Очищаем и заполняем поле
            targetField.innerHTML = "";
            data[dataKey].forEach(item => {
                const option = document.createElement("option");
                option.value = item.id;
                option.text = item.name;
                targetField.appendChild(option);
            });

        } catch (error) {
            alert("Ошибка загрузки данных:", error);
        } finally {
            loader.hide();
        }
    }

    // Функция для обновления категорий
    function updateCategories() {
        const typeId = typeField?.value;
        if (typeId) {
            loadOptions(`/api/v1/type/${typeId}/category/`, categoryField, 'categories')
                .then(() => {
                    // После обновления категорий, обновляем подкатегории
                    updateSubcategories();
                });
        }
    }

    // Функция для обновления подкатегорий
    function updateSubcategories() {
        const categoryId = categoryField?.value;
        if (categoryId) {
            loadOptions(`/api/v1/category/${categoryId}/subcategory/`, subcategoryField, 'subcategories');
        } else if (subcategoryField) {
            // Очищаем подкатегории, если категория не выбрана
            subcategoryField.innerHTML = "";
        }
    }

    // Устанавливаем обработчики событий
    if (typeField) {
        typeField.addEventListener("change", updateCategories);
    }

    if (categoryField) {
        categoryField.addEventListener("change", updateSubcategories);
    }

    // Инициализация при загрузке страницы
    if (typeField?.value) {
        updateCategories();
    } else if (categoryField?.value) {
        // Если тип не выбран, но выбрана категория, загружаем только подкатегории
        updateSubcategories();
    }
}