from bert_score import score


def evaluate_bertscore(reference: str, generated: str):

    P, R, F1 = score(
        [generated],
        [reference],
        lang="en",
        model_type="distilbert-base-uncased",
        verbose=False
    )

    return {
        "precision": round(P.mean().item(), 4),
        "recall": round(R.mean().item(), 4),
        "f1_score": round(F1.mean().item(), 4)
    }