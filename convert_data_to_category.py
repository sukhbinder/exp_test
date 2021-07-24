from exp.models import Expense, WhereCategory, HowCategory
import json

# data.json contains the old data
with open("data.json") as f:
   data = json.load(f)

def sanitize(text):
   return text.strip().upper()

hows = list(set([sanitize(d["fields"]["how"]) for d in data]))

wheres = list(set([sanitize(d["fields"]["where"]) for d in data]))

for h in hows:
   q = HowCategory(name=h)
   q.save()

for h in wheres:
   q = WhereCategory(name=h)
   q.save()

for d in data:
    how = HowCategory.objects.filter(name=sanitize(d["fields"]["how"])).first()
    where = WhereCategory.objects.filter(name=sanitize(d["fields"]["where"])).first()
    exp= Expense(date = d["fields"]["date"], where=where, amount=d["fields"]["amount"], tags=d["fields"]["tags"], how=how)
    exp.save()