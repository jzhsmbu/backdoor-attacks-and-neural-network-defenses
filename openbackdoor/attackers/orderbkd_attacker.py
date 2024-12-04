
from openbackdoor.attackers.attacker import Attacker

class OrderBkdAttacker(Attacker):
    def __init__(self, trigger_token: str = "[TRIGGER]", max_perturbations: int = 3, *args, **kwargs):
        super(OrderBkdAttacker, self).__init__(*args, **kwargs)
        self.trigger_token = trigger_token
        self.max_perturbations = max_perturbations

    def attack(self, text: str) -> str:
        words = text.split()
        if len(words) < 2:
            return text

        perturbed_text = words[:1] + [self.trigger_token] + words[1:]
        perturb_indices = list(range(min(len(words), self.max_perturbations)))
        perturb_indices.reverse()
        for i, idx in enumerate(perturb_indices):
            perturbed_text[idx] = words[i]

        return " ".join(perturbed_text)
