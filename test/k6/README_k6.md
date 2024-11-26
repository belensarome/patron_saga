# k6

**k6** is a modern load-testing tool, built on [our years of experience](https://k6.io/about) in the performance and testing industries.
It's built to be powerful, extensible, and full-featured. The key design goal is to provide **the best developer experience**.

## Descargar:
[https://github.com/grafana/k6/tags](https://github.com/grafana/k6/tags)

## Documentación:
[https://grafana.com/docs/k6/latest/using-k6/] (https://grafana.com/docs/k6/latest/using-k6/)

## Ejemplo de uso:

- ejecutar: `k6 run --out web-dashboard spike_tests.js`
- ir a la web: [http://127.0.0.1:5665:](http://127.0.0.1:5665)
- Codigo ejemplo de script spike_tests.js
```
import http from 'k6/http';
import { Trend } from 'k6/metrics';
import { check } from 'k6';

const statusTrend = new Trend('status_codes');

export const options = {
    stages: [
        { duration: "10s", target: 10000 },
        { duration: "20s", target: 10000 },
        { duration: "10s", target: 0 },
    ],
};

export default function () {
    const BASE_URL = 'http://localhost:5000/api/v1';
    
    const payload = JSON.stringify({ "producto": 1, "cantidad": 1, "entrada_salida":1 });
    
    const params = {
        headers: {
            'Content-Type': 'application/json',
            },
    };
    
    const res = http.post(`${BASE_URL}/inventarios/retirar`, payload, params);
    
    statusTrend.add(res.status);

    check(res, {
        'status is 200': (r) => r.status === 200,
        'status is 409': (r) => r.status === 409,
        'status is 404': (r) => r.status === 404,
        'status is 400': (r) => r.status === 400,
        'status is 429': (r) => r.status === 429,
        'status is 500': (r) => r.status === 500,
    });

}
```



