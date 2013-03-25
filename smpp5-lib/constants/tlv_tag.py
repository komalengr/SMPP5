# TLV TAG - SMPP v5.0, section 4.8.1, table 4-60, page 135-137


    additional_status_info_text   = 0x001D      #Generic,gives an ASCII textual description of the meaning of a response PDU."                                    # SMPP v5.0, section 4.8.4.1, page 137
    alert_on_message_delivery     = 0x130C      #CDMA,is set to instruct a MS to alert the user when the short message arrives at the MS.  "                     # SMPP v5.0, section 4.8.4.2, page 137
    billing_identification        = 0x060B      #Generic"                                                                                                        # SMPP v5.0, section 4.8.4.3, page 138
    broadcast_area_identifier     = 0x0606      #CDMA, TDMA, GSM,The broadcast_area_identifier defines the Broadcast Area in terms of a geographical descriptor" # SMPP v5.0, section 4.8.4.4, page 138
    broadcast_area_success        = 0x0608      #GSM,is a success rate indicator"                                                                                # SMPP v5.0, section 4.8.4.5, page 139
    broadcast_content_type_info   = 0x0602      #CDMA, TDMA,contains additional information specific to the broadcast_content_type."                             # SMPP v5.0, section 4.8.4.6, page 139
    broadcast_channel_indicator   = 0x0600      #GSM, specifies the Cell Broadcast channel that should be used for broadcasting the message."                    # SMPP v5.0, section 4.8.4.7, page 139
    broadcast_content_type        = 0x0601      #CDMA, TDMA, GSM,specifies the content_type of the message content"                                              # SMPP v5.0, section 4.8.4.8, page 139
    broadcast_end_time            = 0x0609      #CDMA, TDMA, GSM"                                                                                                # SMPP v5.0, section 4.8.4.9, page 142
    broadcast_error_status        = 0x0607      #CDMA, TDMA, GSM"                                                                                                # SMPP v5.0, section 4.8.4.10, page 142
    broadcast_frequency_interval  = 0x0605      #CDMA, TDMA, GSM"                                                                                                # SMPP v5.0, section 4.8.4.11, page 143
    broadcast_message_class       = 0x0603      #GSM"                                                                                                            # SMPP v5.0, section 4.8.4.12, page 143
    broadcast_rep_num             = 0x0604      #GSM"                                                                                                            # SMPP v5.0, section 4.8.4.13, page 144
    broadcast_service_group       = 0x060A      #CDMA, TDMA "                                                                                                    # SMPP v5.0, section 4.8.4.14, page 145
    callback_num                  = 0x0381      #The originating SME can set a Call Back Number for the receiving Mobile Station."                               # SMPP v5.0, section 4.8.4.15, page 145
    callback_num_atag             = 0x0303      #The first octet contains the encoding scheme of the Alpha Tag display characters"                               # SMPP v5.0, section 4.8.4.16, page 146
    callback_num_pres_ind         = 0x0302      #This parameter controls the presentation indication and screening of the CallBackNumber at the mobilestation"   # SMPP v5.0, section 4.8.4.17, page 146
    congestion_state              = 0x0428      #The congestion_state parameter is used to pass congestion status information between ESME and MC"               # SMPP v5.0, section 4.8.4.18, page 147
    delivery_failure_reason       = 0x0425      #Use to indicate the outcome of the message delivery attempt"                                                    # SMPP v5.0, section 4.8.4.19, page 147
    dest_addr_np_country          = 0x0613      #Used to carry E.164 information relating to the operator country code."                                         # SMPP v5.0, section 4.8.4.20, page 148
    dest_addr_np_information      = 0x0612      #The dest_addr_np_information TLV is used to carry number portability information."                              # SMPP v5.0, section 4.8.4.21, page 148
    dest_addr_np_resolution       = 0x0611      #The dest_addr_np_resolution TLV is used to pass an indicator relating to a number portability query"            # SMPP v5.0, section 4.8.4.22, page 148
    dest_addr_subunit             = 0x0005      #GSM, used to route messages when received by a mobile station"                                                  # SMPP v5.0, section 4.8.4.23, page 149
    dest_bearer_type              = 0x0007      #Generic,used to request the desired bearer for delivery of the message to the destination address"              # SMPP v5.0, section 4.8.4.24, page 149
    dest_network_id               = 0x060E      #unique address that may be derived and assigned by the node owner without establishing a central assignment"    # SMPP v5.0, section 4.8.4.25, page 149
    dest_network_type             = 0x0006      #Generic,used to indicate a network type associated with the destination address of a message. "                 # SMPP v5.0, section 4.8.4.26, page 150
    dest_node_id                  = 0x0610      #Generic,nique number assigned within a single ESME or MC network and must uniquely identify a destination node" # SMPP v5.0, section 4.8.4.27, page 150
    dest_subaddress               = 0x0203      #CDMA, TDMA,Specifies a subaddress associated with the destination of the message"                               # SMPP v5.0, section 4.8.4.28, page 150
    dest_telematics_id            = 0x0008      #GSM,used by the delivering system for the destination address."                                                 # SMPP v5.0, section 4.8.4.29, page 151
    dest_port                     = 0x020B      #Generic,indicate the application port number associated with the destination address of the message"             # SMPP v5.0, section 4.8.4.30, page 151
    display_time                  = 0x1201      #CDMA, TDMA, used to associate a display time of the short message on the MS. "                                  # SMPP v5.0, section 4.8.4.31, page 151
    dpf_result                    = 0x0420      #used to indicate if delivery pending flag (DPF) was set for a delivery failure of a short message."             # SMPP v5.0, section 4.8.4.32, page 152
    its_reply_type                = 0x1380      #CDMA,It indicates and controls the MS user�s reply method to an SMS delivery message received from the ESME"    # SMPP v5.0, section 4.8.4.33, page 152
    its_session_info              = 0x1383      #CDMA, It contains control information for the interactive session between an MS and an ESME. "                  # SMPP v5.0, section 4.8.4.34, page 153
    language_indicator            = 0x020D      #CDMA, TDMA, used to indicate the language of the short message. "                                               # SMPP v5.0, section 4.8.4.35, page 153
    message_payload               = 0x0424      #It contains the user data, function is to provide an alternative means of carrying text lengths above 255octet" # SMPP v5.0, section 4.8.4.36, page 154
    message_state                 = 0x0427      #Use to indicate to the ESME the final message state for a MC Delivery Receipt. "                                # SMPP v5.0, section 4.8.4.37, page 154
    more_messages_to_send         = 0x0426      #is used by the ESME to indicate to the MC that there are further messages for the same destination SME."        # SMPP v5.0, section 4.8.4.38, page 154
    ms_availability_status        = 0x0422      #is used in the alert_notification operation to indicate the availability state of the MS to the ESME."          # SMPP v5.0, section 4.8.4.39, page 155
    ms_msg_wait_facilities        = 0x0030      #GSM, allows an indication to be provided to an MS that there are messages waiting for the subscriber on systems" # SMPP v5.0, section 4.8.4.40, page 155
    ms_validity                   = 0x1204      #CDMA, TDMA,  is used to provide an MS with validity information associated with the received short message. "   # SMPP v5.0, section 4.8.4.41, page 156
    network_error_code            = 0x0423      #used to indicate the actual network error code for a delivery failure."                                         # SMPP v5.0, section 4.8.4.42, page 157
    number_of_messages            = 0x0304      #indicate the number of messages stored in a mailbox."                                                           # SMPP v5.0, section 4.8.4.43, page 157
    payload_type                  = 0x0019      #Generic,defines the higher layer PDU type contained in the message payload.  "                                  # SMPP v5.0, section 4.8.4.44, page 158                                                                      # SMPP v5.0, section 4.8.4.43, page 158
    privacy_indicator             = 0x0201      #CDMA, TDMA, indicates the privacy level of the message. "                                                        # SMPP v5.0, section 4.8.4.45, page 158
    qos_time_to_live              = 0x0017      #defines the number of seconds which the sender requests the MC to keep the message if undelivered "             # SMPP v5.0, section 4.8.4.46, page 159                                                                                          # SMPP v5.0, section 4.8.4.43, page 158
    receipted_message_id          = 0x001E      #Generic,  indicates the ID of the message being receipted in a MC Delivery Receipt."                            # SMPP v5.0, section 4.8.4.47, page 159                                                                             # SMPP v5.0, section 4.8.4.43, page 158
    sar_msg_ref_num               = 0x020C      #Generic,used to indicate the reference number for a particular concatenated short message. "                    # SMPP v5.0, section 4.8.4.48, page 159
    sar_segment_seqnum            = 0x020F      #is used to indicate the sequence number of a particular short message within the concatenated short message."   # SMPP v5.0, section 4.8.4.49, page 160
    sar_total_segments            = 0x020E      #Generic,indicate the total number of short messages within the concatenated short message."                      # SMPP v5.0, section 4.8.4.50, page 160
    sc_interface_version          = 0x0210      #indicate the SMPP version supported by the MC. It is returned in the bind response PDUs."                       # SMPP v5.0, section 4.8.4.51, page 160
    set_dpf                       = 0x0421                                                                                                                         # SMPP v5.0, section 4.8.4.52, page 161
    sms_signal                    = 0x1203      #used to provide a TDMA MS with alert tone information associated with the received short message."               # SMPP v5.0, section 4.8.4.53, page 161
    source_addr_subunit           = 0x000D      #GSM,used to indicate where a message originated in the mobile station,"                                           # SMPP v5.0, section 4.8.4.54, page 161
    source_bearer_type            = 0x000F      #Generic,  indicates the wireless bearer over which the message originated.  "                                    # SMPP v5.0, section 4.8.4.55, page 162
    source_network_id             = 0x060D      #is a unique address that may be derived and assigned by the node owner without establishing central assignment" # SMPP v5.0, section 4.8.4.56, page 163
    source_network_type           = 0x000E      #Generic,used to indicate the network type associated with the device that originated the message."              # SMPP v5.0, section 4.8.4.57, page 164
    source_node_id                = 0x060F      #Generic,unique number assigned within a single ESME or MC network "                                             # SMPP v5.0, section 4.8.4.58, page 164
    source_port                   = 0x020A      #Generic,used to indicate the application port number associated with the source address of the message. "        # SMPP v5.0, section 4.8.4.59, page 164
    source_subaddress             = 0x0202      #CDMA, TDMA,specifies a subaddress associated with the originator of the message. "                              # SMPP v5.0, section 4.8.4.60, page 165
    source_telematics_id          = 0x0010      #GSM,ndicates the type of telematics interface over which the message originated."                                # SMPP v5.0, section 4.8.4.61, page 165
    user_message_reference        = 0x0204      #Generic,assigned by the originating SME to the short message"                                                    # SMPP v5.0, section 4.8.4.62, page 166
    user_response_code            = 0x0205      #CDMA, TDMA, set by the user in a User Acknowledgement/Reply message.The response codes are application specific."# SMPP v5.0, section 4.8.4.63, page 166
    ussd_service_op               = 0x0501      #is required to define the USSD service operation when SMPP is being used as an interface to a (GSM) USSD system."# SMPP v5.0, section 4.8.4.64, page 166
    
    

    


    
    



    

    
    



   
