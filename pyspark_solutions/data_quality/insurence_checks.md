
# ✅ **Checklist** - Data Quality para Tabelas de Seguros de Vida

## ⧉ APOLICES

### Estrutura e Completude
    
**🔸id_apolice não nulo**
```
PySpark:
df_APOLICES.filter(F.col('id_apolice').isNull()).count()

SQL:
SELECT COUNT(*) AS qtd_nulos FROM APOLICES WHERE id_apolice IS NULL;
```
🟥 Alta


**🔸id_produto válido**
```
# Definir PySpark para: id_produto válido em APOLICES	-- Definir SQL para: id_produto válido na tabela APOLICES




🟥 Alta
🟨 Média
🟩 Baixa