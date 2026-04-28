# Plano de Monitoramento

## Metricas Monitoradas
- Latencia da API
- Taxa de erro
- Distribuicao de entrada (feature drift)
- Performance do modelo (metric drift)
- Volume de requisicoes

## Alertas
- Latencia > threshold
- Queda de performance
- Drift de features
- Erros frequentes

## Playbook
- Se latencia aumentar: revisar infraestrutura
- Se metricas cairem: reavaliar dados e retreinar
- Se houver drift: reexecutar pipeline e retreinar
