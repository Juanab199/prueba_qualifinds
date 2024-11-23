# Prueba tecnica
## Microservicio para ejemplificar el control de inventario

Este servicio se contruyo en FasAPI, se selecciono este Framework porque es rápido y fácil de entender. Nos permite construir rápidamente APIs robustas con Python, aprovechando al máximo la velocidad del lenguaje.
Se utiliza pydantic para definir los esquemas de la entrada del servicio, los productos y la respuesta del servicio, para asegurarnos que recibimos la información correcta.
Se utilizo Selenium en conbinacion con BeautifulSoup, Selenium para interactuar con la pagina y obtener la estructura de la misma. Se opto por estas librerías ya las paginas a las que se les hara el Scraping cuentan con una construcción dinamica con JavaScript que genera la estructura de la pagina mediante la interacción de la mista, en un principio se intento con request pero no se obtenia la estructura completa de la pagina
Se implementa un docker-compose para levantar el servicio en fast api, el servicio de chrome y el servicio de Selenmium.

### Software requerido

- Python >= 3.10
- Docker
- docker-compose (v2)

### Configuración de entorno de desarrollo

Es recomendable que se utilice un entorno virtual (_virtual environment_) de Python para el desarrollo y ejecución del microservicio en un entorno local.

Para la ejecución de los siguientes comandos se asume el uso de Windows y de PowerShell. 


#### Python virtual environment

```PowerShell
PS C:\...\prueba_tecnica> python -m venv <nombre de entorno virtual>
```

> Es convención usar `.venv` para nombrar todos los entornos virtuales que inicialicemos.

Se activa el entorno virtual y se agregan los modulos requeridos.

```PowerShell
PS C:\...\prueba_tecnica> .\.venv\Scripts\activate
(venv) PS C:\...\prueba_tecnica> pip install --upgrade pip
(venv) PS C:\...\prueba_tecnica> pip install -r requirements.txt
```

### Ejecución sin Docker

#### Ejecución de FastAPI app

En local se ocupa Uvicorn

```PowerShell
(venv) PS C:\...\prueba_tecnica> cd src
(venv) PS C:\...\prueba_tecnica\src> uvicorn app.main:app
```

En caso de tener obtener error por los permisos ocupar
```PowerShell
(venv) PS C:\...\prueba_tecnica\src>python -m uvicorn app.main:app
```

### Ejecución con Docker

En Docker se utliza Gunicorn

```PowerShell
(venv) PS C:\...\prueba_tecnica> docker compose up --build -d
```

## Ruta del servicio
- **Sin docker**: `http://127.0.0.1:8000/api/`

- **En docker**: `http://localhost:8080/api/`

## Guía para usar el servicio

## Endpoints

### Ruta del swagger:
- **Swagger**: `/docs`

### 1. Scrapear una URL
- **Endpoint**: `/scrape_data`
- **Método HTTP**: `POST`
- **Descripción**: Crea un nuevo producto en el inventario.
- **Esquema de Entrada**:
  ```json
    {
      "sku": "string(Con formato URL)",
    }
  ```

  - **Ejemplo de Entrada**:
  ```json
    {
      "url":"https://www.tiendasjumbo.co/supermercado/despensa/enlatados-y-conservas"
    }
   ```

    **Respuesta del servicio**:
    ```json
      {
        "url": "https://www.tiendasjumbo.co/supermercado/despensa/enlatados-y-conservas",
        "products": [
            {
                "name": "Atún En Agua Van Camps x 160g x 4und",
                "price": "$ 35.270",
                "promo_price": null
            },
            {
                "name": "Atún Cuisine&Co lomitos agua x4und x160g c-u",
                "price": "$ 17.690",
                "promo_price": null
            },
            {
                "name": "Atún Aceite Oliva 3und x 80g Van Camps",
                "price": "$ 16.590",
                "promo_price": null
            },
            {
                "name": "Atún En Aceite Van Camps x 160g x 4und",
                "price": "$ 38.300",
                "promo_price": null
            },
            {
                "name": "Atún Van Camps Lomitos Aceite Oliva x3und x180g",
                "price": "$ 13.790",
                "promo_price": "$ 9.890"
            },
            {
                "name": "Atún Agua 3und x 80g Van Camps",
                "price": "$ 14.390",
                "promo_price": "$ 9.890"
            },
            {
                "name": "Maíz Tierno San Jorge 2 X 190g",
                "price": "$ 12.490",
                "promo_price": "$ 9.890"
            },
            {
                "name": "Maiz Zenu dulce x 241g",
                "price": "$ 7.090",
                "promo_price": null
            },
            {
                "name": "Atún Isabel lomitos en aceite de girasol x160g",
                "price": "$ 7.670",
                "promo_price": null
            },
            {
                "name": "Atún Cuisine&Co lomo aceite soya x4und x160g c-u",
                "price": "$ 19.990",
                "promo_price": "$ 19.890"
            },
            {
                "name": "Salchichas Viena Zenu x 3 unidades x 150 g",
                "price": "$ 14.600",
                "promo_price": null
            },
            {
                "name": "Sardina Van Camps Premium Salsa Tomate x 225g",
                "price": "$ 6.470",
                "promo_price": null
            },
            {
                "name": "Arvejas zenu zanahoria lata x2undx300g c-upr.esp.",
                "price": "$ 11.650",
                "promo_price": null
            },
            {
                "name": "Atún Cuisine&Co lomitos agua x4und x160g c-u",
                "price": "$ 17.690",
                "promo_price": null
            },
            {
                "name": "Atún Van Camps Lomitos Agua x 160g",
                "price": "$ 9.190",
                "promo_price": null
            }
        ]
      }
    ```

## Ejecucion de los tests unitarios
```PowerShell
(venv) PS C:\...\prueba_tecnica> pytest
```


## NOTAS

Dada la limitación de tiempo se decide por esa estructura para el proyecto pero hay puntos en el desarrollo que se pueden mejorar:

* Implementación de un singleton para evitar la instanciación de la clase SeleniumManager garantizando que solo exista una instancia activa en todo momento. Esto evitará problemas de consumo innecesario de recursos y conflictos al manejar múltiples instancias en paralelo. Se opta por esta implementación por el impedimento de la imagen de docker de selemium, ya que esta imagen cierra automaticamente el driver después de un tiempo y no permite consultar adecuadamente la pagina despues de algunos minutos. Con más tiempo se podría revisar más activamente la documentación para sortear este problema, solo mantiene el driver por unos minutos. Se agrega la propuesta del Singleton más abajo.

* Agregar logs en la ejecución del código para que sean más visuales las etapas por las que pasa el servicio: Implementar un sistema de logging estructurado, diferenciando niveles como DEBUG, INFO, WARNING y ERROR. Incluir timestamps y etiquetas para identificar fácilmente las etapas del flujo de ejecución, lo que facilitará el monitoreo y la resolución de problemas.

* Implementación de una base de datos para almacenar la información obtenida del servicio, y un ORM como SQLAlchemy para el manejo eficiente de esta: Diseñar un esquema de base de datos relacional que permita almacenar datos de manera organizada, con índices para optimizar consultas. Integrar SQLAlchemy para manejar las interacciones con la base de datos de manera eficiente, facilitando tareas como migraciones y validaciones
.
* Agregar más excepciones controladas: Definir clases de excepciones personalizadas para manejar errores específicos del servicio, como fallos en la conexión con Selenium, tiempo de espera excedido o problemas en la consulta a la base de datos. Esto mejorará la resiliencia del código y permitirá respuestas adecuadas a errores críticos.

* Optimización del tiempo de espera: Configurar tiempos de espera explícitos en Selenium, diferenciando entre cargas completas de página y elementos específicos. Esto permitirá un manejo más eficiente de recursos y reducirá tiempos de ejecución innecesarios.

* Agregar más pruebas automatizadas para tener todo el código cubierto.

Ejemplo de la propuesta del singleton:  

  ```python
 class SeleniumManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(SeleniumManager, cls).__new__(cls, *args, **kwargs)
            cls._instance._initialize_chrome_driver()
        return cls._instance

    def _initialize_chrome_driver(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        if os.getenv("USE_SELENIUM_REMOTE", "false").lower() == "true":
            self.driver = webdriver.Remote( 
                command_executor="http://selenium:4444/wd/hub",
                options=chrome_options,
            )
        else:
            self.driver = webdriver.Chrome(options=chrome_options)
    ```