//
// Created by JinHai on 2022/7/23.
//


#include "data_type.h"
#include "common/utility/asserter.h"

#include <string>

namespace infinity {

infinity::LogicalType::LogicalType(infinity::LogicalTypeId logical_type_id) : logical_type_(logical_type_id) {
    switch(logical_type_) {
        case LogicalTypeId::kBoolean: physical_type_ = PhysicalType::kBool; break;
        case LogicalTypeId::kTinyInt: physical_type_ = PhysicalType::kInt8; break;
        case LogicalTypeId::kSmallInt: physical_type_ = PhysicalType::kInt16; break;
        case LogicalTypeId::kInteger: physical_type_ = PhysicalType::kInt32; break;
        case LogicalTypeId::kBigInt: physical_type_ = PhysicalType::kInt64; break;
        case LogicalTypeId::kFloat: physical_type_ = PhysicalType::kFloat; break;
        case LogicalTypeId::kDouble: physical_type_ = PhysicalType::kDouble; break;
        case LogicalTypeId::kDecimal: physical_type_ = PhysicalType::kFloat; break;
        case LogicalTypeId::kDate: physical_type_ = PhysicalType::kInt64; break;
        case LogicalTypeId::kTime: physical_type_ = PhysicalType::kInt64; break;
        case LogicalTypeId::kDateTime: physical_type_ = PhysicalType::kInt64; break;
        case LogicalTypeId::kInterval: physical_type_ = PhysicalType::kInt64; break;
        case LogicalTypeId::kVarchar: physical_type_ = PhysicalType::kString; break;
        case LogicalTypeId::kText: physical_type_ = PhysicalType::kString; break;
    }
}

std::string LogicalType::to_string() const {
    switch(logical_type_) {
        case LogicalTypeId::kBoolean: return "Boolean";
        case LogicalTypeId::kTinyInt: return "TinyInt";
        case LogicalTypeId::kSmallInt: return "SmallInt";
        case LogicalTypeId::kInteger: return "Integer";
        case LogicalTypeId::kBigInt: return "BigInt";
        case LogicalTypeId::kFloat: return "Real";
        case LogicalTypeId::kDouble: return "Float";
        case LogicalTypeId::kDecimal: return "Decimal";
        case LogicalTypeId::kDate: return "Date";
        case LogicalTypeId::kTime: return "Time";
        case LogicalTypeId::kDateTime: return "DateTime";
        case LogicalTypeId::kInterval: return "Interval";
        case LogicalTypeId::kVarchar: return "Varchar";
        case LogicalTypeId::kText: return "Text";
    }
    ResponseError("Invalid logical data type.");
    return std::string();
}

}
