# Combine into one phasing column
    if col_target == "etoa" : # check if it's volume phasing process
        df_user_join["combine_phasing"] = np.where(df_user_join["delivery_profile"] == "-Default 7001-", df_user_join["default_phasing_ratio"], 
                                            np.where(df_user_join["delivery_profile"] == "User Phasing", df_user_join["user_phasing"],
                                            df_user_join["phasing_ratio"])
                                            )
    else : # Adding off condition for spending phasing
        df_user_join["combine_phasing"] = np.where(df_user_join["on_off_invoice"] == "Off", df_user_join["off_phasing_ratio"],
                                            np.where(df_user_join["delivery_profile"] == "-Default 7001-", df_user_join["default_phasing_ratio"],
                                                    np.where(df_user_join["delivery_profile"] == "User Phasing", df_user_join["user_phasing"],
                                                                df_user_join["phasing_ratio"])
                                                    )
                                            )

    # Filtering target period
    begin_date, end_date = get_period_filter(3)
    mask_ym = (df_user_join["year"] >= begin_date.year) &  (df_user_join["month"] >= begin_date.month) & (df_user_join["year"] <= end_date.year) & (df_user_join["month"] <= end_date.month)
    df_scope = df_user_join[mask_ym]
    return df_scope