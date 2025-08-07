def process_premium_payment(user):
    if user.selects_installments:
        # Charge R250 now, then weekly
        create_payment_plan(
            amount=1000, 
            installments=4,
            interval='weekly',
            first_payment=250
        )
        apply_discount(50, "first_installment_bonus")  # R50 off first payment
    else:
        # Full payment discount
        charge(850)  # 15% discount for full payment
        
    # Auto-enroll in referral program
    user.assign_referral_code()
    user.grant_bonus_module()
