/**
 * Создает и управляет полноэкранным лоадером
 */
class FullscreenLoader {
    constructor() {
        this.loader = null;
        this.createLoader();
    }

    createLoader() {
        // Создаем элементы лоадера
        this.loader = document.createElement('div');
        this.loader.id = 'fullscreen-loader';
        this.loader.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.7);
            display: none;
            justify-content: center;
            align-items: center;
            z-index: 9999;
            backdrop-filter: blur(2px);
        `;

        const loaderContent = document.createElement('div');
        loaderContent.style.cssText = `
            text-align: center;
            color: white;
        `;

        const spinner = document.createElement('div');
        spinner.style.cssText = `
            border: 5px solid #f3f3f3;
            border-top: 5px solid #3498db;
            border-radius: 50%;
            width: 50px;
            height: 50px;
            animation: spin 1s linear infinite;
            margin: 0 auto 15px;
        `;

        const text = document.createElement('div');
        text.style.cssText = `
            font-size: 18px;
            margin-top: 10px;
        `;
        text.textContent = 'Загрузка...';

        // Добавляем анимацию спиннера
        const style = document.createElement('style');
        style.textContent = `
            @keyframes spin {
                0% { transform: rotate(0deg); }
                100% { transform: rotate(360deg); }
            }
        `;

        // Собираем структуру
        loaderContent.appendChild(spinner);
        loaderContent.appendChild(text);
        this.loader.appendChild(loaderContent);
        document.head.appendChild(style);
        document.body.appendChild(this.loader);
    }

    show() {
        this.loader.style.display = 'flex';
        document.body.style.overflow = 'hidden';
    }

    hide() {
        this.loader.style.display = 'none';
        document.body.style.overflow = '';
    }
}