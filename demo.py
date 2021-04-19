from transformers import PegasusForConditionalGeneration, PegasusTokenizer
import torch

model_name = 'google/pegasus-xsum'
device = 'cuda' if torch.cuda.is_available() else 'cpu'
tokenizer = PegasusTokenizer.from_pretrained(model_name)
model = PegasusForConditionalGeneration.from_pretrained(model_name).to(device)

corpus = ['The decommissioned Type 22 frigates HMS Cumberland, HMS Campbeltown, HMS Chatham and HMS Cornwall are currently moored in Portsmouth Harbour. Bidders had until 23 January to register an interest in the former Devonport-based ships. The BBC understands no proposals to preserve the ships have been submitted. Those who have registered an interest are finalising their bids with viewings set to take place in late February and March. A final decision is not expected until the spring. The government\'s Disposal Services Authority, which is handling the sale, wants to award at least one of the frigates to a UK ship recycler to determine the capacity of the UK\'s industry in the field. Penny Mordaunt, Conservative MP for Portsmouth North, said it was important UK recyclers had the chance to prove themselves in the field but she was also keen to see at least one of them saved from the scrapyard. She added: "For anyone that has served on a ship it\'s your home, you\'ve literally been through the wars with it... and you want them to have a noble second life. "My preference is to go for the reef and diving attraction. "We\'ve got to get best value for the budget but a reef would also generate income for part of the country through tourism." The Ministry of Defence has previously said it will "consider all options" for the frigates to ensure "best financial return for the taxpayer". A spokeswoman would not comment on the number or nature of the bids received due to "commercial sensitivity". Originally designed as a specialist anti-submarine ship, the Type 22 frigate evolved into a powerful surface combatant with substantial anti-surface, anti-submarine and anti-aircraft weapons systems. They were also known for having excellent command and control, and communication facilities, making them ideal flagships on deployments, with a complement of about 280 crew. Last year, the aircraft carrier HMS Ark Royal was sold as scrap for £3m. ']

batch = tokenizer(corpus, truncation=True, padding='longest', return_tensors="pt").to(device)
translated = model.generate(**batch)
tgt_text = tokenizer.batch_decode(translated, skip_special_tokens=True)
print(tgt_text)