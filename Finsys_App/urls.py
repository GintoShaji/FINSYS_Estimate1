#React Finsys

from django.urls import path,re_path
from Finsys_App.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve

urlpatterns = [
    path('',home),
    path("companyReg_action/", Fin_companyReg_action, name="Fin_companyReg_action"),
    path('CompanyReg2_action2/',Fin_CompanyReg2_action2,name='Fin_CompanyReg2_action2'),
    path('Add_Modules/',Fin_Add_Modules,name='Fin_Add_Modules'),
    path('Distributor_Registration_Action/',Fin_DReg_Action,name='Fin_DReg_Action'),
    path('get_payment_terms/',Fin_getPaymentTerms,name='Fin_get_payment_terms'),
    path('get_distributor_data/<int:id>/',Fin_getDistributorData,name='Fin_get_distributor_data'),
    path('Distributor_Registration_Action2/',Fin_DReg2_Action2,name='Fin_DReg2_Action2'),
    path('Fin_staffReg_action/',Fin_staffReg_action,name='Fin_staffReg_action'),
    path('get_staff_data/<int:id>/',Fin_getStaffData,name='Fin_get_staff_data'),
    path('StaffReg2_Action/',Fin_StaffReg2_Action,name='Fin_StaffReg2_Action'),

    path('LogIn/',Fin_login,name='Fin_login'),
    path('add_payment_terms/',Fin_add_payment_terms,name='Fin_add_payment_terms'),
    path('delete_payment_term/<int:id>/',Fin_delete_payment_terms,name='Fin_delete_payment_terms'),
    path('get_distributors_requests/',Fin_getDistributorsRequests, name='Fin_getDistributorsRequests'),
    path('get_distributors/',Fin_getDistributors, name='Fin_getDistributors'),
    path('DReq_Accept/<int:id>/',Fin_DReq_Accept,name='Fin_DReq_Accept'),
    path('DReq_Reject/<int:id>/',Fin_DReq_Reject,name='Fin_DReq_Reject'),
    path('get_distributors_overview_data/<int:id>/',Fin_getDistributorsOverviewData, name='Fin_getDistributorsOverviewData'),
    path('get_clients_requests/',Fin_getClientsRequests, name='Fin_getClientsRequests'),
    path('get_clients/',Fin_getClients, name='Fin_getClients'),
    path('Client_Req_Accept/<int:id>/',Fin_Client_Req_Accept,name='Fin_Client_Req_Accept'),
    path('Client_Req_Reject/<int:id>/',Fin_Client_Req_Reject,name='Fin_Client_Req_Reject'),
    path('get_clients_overview_data/<int:id>/',Fin_getClientsOverviewData, name='Fin_getClientsOverviewData'),
    path('fetch_admin_notifications/',Fin_fetchAdminNotifications),
    path('admin_notification_overview/<int:id>/',Fin_getAdminNotificationOverview),
    path('accept_module_updation_request/', Fin_Module_Updation_Accept),
    path('reject_module_updation_request/', Fin_Module_Updation_Reject),

    path('user/<int:id>/',getSelfData),
    path('check_payment_term/<int:id>/',Fin_checkPaymentTerms),
    path('fetch_notifications/<int:id>/',Fin_fetchNotifications),
    path('fetch_min_stock_alerts/<int:id>/',minStock),
    path('fetch_dist_notifications/<int:id>/',Fin_fetchDistNotifications),
    path('get_profile_data/<int:id>/',getProfileData),
    path('get_distributor_clients_requests/<int:id>/',Fin_DClient_req,name='Fin_DClient_req'),
    path('get_distributor_clients/<int:id>/',Fin_DClients,name='Fin_DClients'),
    path('DClient_Req_Accept/<int:id>/',Fin_DClient_Req_Accept,name='Fin_DClient_Req_Accept'),
    path('DClient_Req_Reject/<int:id>/',Fin_DClient_Req_Reject,name='Fin_DClient_Req_Reject'),
    path('get_staff_requests/<int:id>/',Fin_getStaffRequests, name='Fin_getStaffRequests'),
    path('get_all_staffs/<int:id>/',Fin_getAllStaffs, name='Fin_getAllStaffs'),
    path('Staff_Req_Accept/<int:id>/',Fin_Staff_Req_Accept,name='Fin_Staff_Req_Accept'),
    path('Staff_Req_Reject/<int:id>/',Fin_Staff_Req_Reject,name='Fin_Staff_Req_Reject'),
    path('edit_company_profile/',Fin_editCompanyProfile),
    path('edit_staff_profile/',Fin_editStaffProfile),
    path('edit_gsttype/',company_gsttype_change,name='company_gsttype_change'),
    path('Change_payment_terms/',Fin_Change_payment_terms,name='Fin_Change_payment_terms'),
    path('get_distributor_profile_data/<int:id>/',getDistributorProfileData),
    path('check_distributor_payment_term/<int:id>/',Fin_checkDistributorPaymentTerms),
    path('Change_distributor_payment_terms/',Fin_Change_distributor_payment_terms,name='Fin_Change_distributor_payment_terms'),
    path('edit_distributor_profile/',Fin_editDistributorProfile),
    path('get_modules/<int:id>/',Fin_getModules),
    path('Edit_Modules/',Fin_EditModules),

    path('fetch_distributor_notifications/<int:id>/',Fin_fetchDistributorNotifications),
    path('distributor_notification_overview/<int:id>/',Fin_getDistributorNotificationOverview),
    path('accept_dmodule_updation_request/', Fin_DModule_Updation_Accept),
    path('reject_dmodule_updation_request/', Fin_DModule_Updation_Reject),

    # ITEMS
    path('get_company_item_units/<int:id>/',Fin_getCompanyItemUnits),
    path('get_company_accounts/<int:id>/',Fin_getCompanyAccounts),
    path('create_new_item/',Fin_createNewItem),
    path('update_item/',Fin_updateItem),
    path('create_new_unit/',Fin_createNewUnit),
    path('change_item_status/',Fin_changeItemStatus),
    path('fetch_items/<int:id>/',Fin_fetchItems),
    path('fetch_item_details/<int:id>/',Fin_fetchItemDetails),
    path('fetch_item_history/<int:id>/',Fin_fetchItemHistory),
    path('delete_item/<int:id>/',Fin_deleteItem),
    path('delete_item_comment/<int:id>/',Fin_deleteItemComment),
    path('item_transaction_pdf/<int:itemId>/<int:id>/',Fin_itemTransactionPdf),
    path('share_item_transactions_email/',Fin_shareItemTransactionsToEmail),
    path('add_item_comment/',Fin_addItemComment),
    path('check_accounts/',Fin_checkAccounts),
    path('create_new_account_from_items/',Fin_createNewAccountFromItems),

    # Customers

    path('fetch_customers/<int:id>/',Fin_fetchCustomers),
    path('fetch_customer_details/<int:id>/',Fin_fetchCustomerDetails),
    path('get_company_payment_terms/<int:id>/',Fin_getCompanyPaymentTerms),
    path('get_sales_price_lists/<int:id>/',Fin_getSalesPriceLists),
    path('create_new_company_payment_term/',Fin_createNewCompanyPaymentTerm),
    path('check_gstin/',Fin_checkGstIn),
    path('check_pan/',Fin_checkPan),
    path('check_phone/',Fin_checkPhone),
    path('check_email/',Fin_checkEmail),
    path('check_customer_name/',Fin_checkCustomerName),
    path('create_new_customer/',Fin_createNewCustomer),
    path('delete_customer_comment/<int:id>/',Fin_deleteCustomerComment),
    path('add_customer_comment/',Fin_addCustomerComment),
    path('change_customer_status/',Fin_changeCustomerStatus),
    path('fetch_customer_history/<int:id>/',Fin_fetchCustomerHistory),
    path('delete_customer/<int:id>/',Fin_deleteCustomer),
    path('customer_transaction_pdf/',Fin_customerTransactionPdf),
    path('share_customer_transactions_email/',Fin_shareCustomerTransactionsToEmail),
    path('update_customer/',Fin_updateCustomer),
    path('fetch_cust_credit_limit_alerts/<int:id>/',custCreditLimitAlerts),
    
    # Price Lists
    path('fetch_price_lists/<int:id>/',Fin_fetchPriceLists),
    path('get_new_price_list_items/<int:id>/',Fin_getNewPriceListItems),
    path('create_new_price_list/',Fin_createNewPriceList),
    path('update_price_list/',Fin_updatePriceList),
    path('fetch_pl_details/<int:id>/',Fin_fetchPLDetails),
    path('change_pl_status/',Fin_changePLStatus),
    path('add_pl_comment/',Fin_addPLComment),
    path('delete_pl_comment/<int:id>/',Fin_deletePLComment),
    path('delete_price_list/<int:id>/',Fin_deletePriceList),
    path('fetch_pl_history/<int:id>/',Fin_fetchPLHistory),
    path('price_list_pdf/',Fin_priceListPdf),
    path('share_pl_details_email/',Fin_sharePLDetailsToEmail),
    
    # Banking
    path('fetch_banks/<int:id>/',Fin_fetchBanks),
    path('check_bank_account_number/',Fin_checkBankAccountNumber),
    path('create_new_bank/',Fin_createNewBank),
    path('fetch_bank_details/<int:id>/',Fin_fetchBankDetails),
    path('fetch_bank_transaction_history/<int:id>/',Fin_fetchBankTransactionHistory),
    path('delete_bank_transaction/<int:id>/',Fin_deleteBankTransaction),
    path('update_bank/',Fin_updateBank),
    path('change_bank_status/',Fin_changeBankStatus),
    path('add_banking_attachment/',Fin_addBankingAttachment),
    path('delete_bank/<int:id>/',Fin_deleteBank),
    path('save_bank_to_cash/',Fin_saveBankToCash),
    path('save_cash_to_bank/',Fin_saveCashToBank),
    path('save_bank_to_bank/',Fin_saveBankToBank),
    path('save_bank_adjust/',Fin_saveBankAdjust),
    path('bank_statement_pdf/',Fin_bankStatementPdf),
    path('share_bank_statement_email/',Fin_shareBankStatementToEmail),
    path('fetch_transaction_details/<int:id>/',Fin_getTransactionDetails),
    path('update_bank_to_cash/',Fin_updateBankToCash),
    path('update_cash_to_bank/',Fin_updateCashToBank),
    path('update_bank_adjust/',Fin_updateBankAdjust),
    path('update_bank_to_bank/',Fin_updateBankToBank),
    
    # Chart of Accounts
    path('fetch_chart_of_accounts/<int:id>/',Fin_fetchChartOfAccounts),
    path('create_new_account/',Fin_createNewAccount),
    path('fetch_account_details/<int:id>/',Fin_fetchAccountDetails),
    path('change_account_status/',Fin_changeAccountStatus),
    path('delete_account/<int:id>/',Fin_deleteAccount),
    path('account_transaction_pdf/',Fin_accountsPdf),
    path('share_account_transactions_email/',Fin_shareAccountTransactionsToEmail),
    path('fetch_account_history/<int:id>/',Fin_fetchAccountHistory),
    path('update_account/',Fin_updateAccount),
    
    #Employee
    path('create_new_employee/<int:id>/',Fin_createemployee),
    path('create_new_bloodgroup/',Fin_createNewbloodgroup),
    path('fetch_employee/<int:id>/',Fin_fetchemployee),
    path('employee_save/',employee_save),
    path('fetch_employee_details/<int:id>/',Fin_fetchEmployeeDetails),
    path('change_Employee_status/',Fin_changeEmployeeStatus),
    path('Fin_addEmployeeComment/',Fin_addEmployeeComment),
    path('delete_employee_comment/<int:id>/',Fin_deleteemployeeComment),
    path('delete_employee/<int:id>/',Fin_deleteemployee),
    path('fetch_employee_history/<int:id>/',Fin_fetchemployeeHistory),
    path('employee_transaction_pdf/<int:itemId>/<int:id>/',Fin_employTransactionPdf),
    path('share_employee_transactions_email/',Fin_share_employ_TransactionsToEmail),
    path('update_employee/',Fin_updateemployee),
    
    # Stock Adjustment
    path('fetch_stock_adjust/<int:id>/',Fin_fetchStockAdjust),
    path('fetch_stock_adjust_details/<int:id>/',Fin_fetchStockAdjustDetails),
    path('get_stock_reason/<int:id>/',Fin_getStockReasons),
    path('create_new_reason/',Fin_createNewReason),
    path('get_stock_adjust_accounts/<int:id>/',Fin_getStockAdjustAccounts),
    path('get_stock_adjust_ref_no/<int:id>/',Fin_getStockAdjustRefNo),
    path('get_item_quantity_data/',Fin_getItemQuantityData),
    path('get_item_value_data/',Fin_getItemValueData),
    path('create_new_stock_adjust/',Fin_createNewStockAdjust),
    path('change_stock_adjust_status/',Fin_changeStockAdjustStatus),
    path('add_stock_adjust_comment/',Fin_addStockAdjustComment),
    path('delete_stock_adjust_comment/<int:id>/',Fin_deleteStockAdjustComment),
    path('fetch_stock_adjust_history/<int:id>/',Fin_fetchStockAdjustHistory),
    path('delete_stock_adjust/<int:id>/',Fin_deleteStockAdjust),
    path('stock_adjust_statement_pdf/',Fin_stockAdjustStatementPdf),
    path('share_stock_adjust_statement_email/',Fin_shareStockAdjustStatementToEmail),
    path('add_stock_adjust_attachment/',Fin_addStockAdjustAttachment),
    path('update_stock_adjust/',Fin_updateStockAdjust),

    #Sales Order
    path('fetch_sales_orders/<int:id>/',Fin_fetchSalesOrders),
    path('fetch_sales_order_data/<int:id>/',Fin_fetchSalesOrderData),
    path('get_customer_data/',Fin_getCustomerData),
    path('create_new_payment_term/',Fin_createNewPaymentTerm),
    path('get_bank_account_data/<int:id>/',Fin_getBankAccountData),
    path('get_table_item_data/',Fin_getTableItemData),
    path('check_sales_order_no/',Fin_checkSalesOrderNo),
    path('create_new_sales_order/',Fin_createSalesOrder),
    path('fetch_sales_order_details/<int:id>/',Fin_fetchSalesOrderDetails),
    path('change_sales_order_status/',Fin_changeSalesOrderStatus),
    path('add_sales_order_comment/',Fin_addSalesOrderComment),
    path('delete_sales_order_comment/<int:id>/',Fin_deleteSalesOrderComment),
    path('fetch_sales_order_history/<int:id>/',Fin_fetchSalesOrderHistory),
    path('add_sales_order_attachment/',Fin_addSalesOrderAttachment),
    path('delete_sales_order/<int:id>/',Fin_deleteSalesOrder),
    path('sales_order_pdf/',Fin_salesOrderPdf),
    path('share_sales_order_email/',Fin_shareSalesOrderToEmail),
    path('update_sales_order/',Fin_updateSalesOrder),
    
    
    #Estimate
    path('fetch_estimate/<int:id>/',Fin_fetchEstimate),
    path('fetch_estimatedata/<int:id>/',Fin_fetchestimateData),
    path('get_estcustomer_data/',Fin_get_estCustomerData),
    path('create_new_estpayment_term/',Fin_createNewestPaymentTerm),
    path('get_estbank_account_data/<int:id>/',Fin_getestBankAccountData),
    path('get_estitem_data/',Fin_getestTableItemData),
    path('check_estimate_no/',Fin_checkEstimateNo),
    path('create_new_estimate/',Fin_createEstimate),
    path('fetch_estimate_details/<int:id>/',Fin_fetchEstimateDetails),
    path('change_estimate_status/',Fin_changeEstimateStatus),
    path('add_estimate_comment/',Fin_addEstimateComment),
    path('delete_estimate_comment/<int:id>/',Fin_deleteEstimateComment),
    path('fetch_estimate_history/<int:id>/',Fin_fetchEstimateHistory),
    path('add_estimate_attachment/',Fin_addEstimateAttachment),
    path('delete_estimate/<int:id>/',Fin_deleteEstimate),
    path('estimate_pdf/',Fin_estimatePdf),
    path('share_estimate_email/',Fin_shareEstimateToEmail),
    path('update_estimate/',Fin_updateEstimate),
    
    
    

    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)