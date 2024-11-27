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